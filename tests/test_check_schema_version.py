import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / "scripts" / "check_schema_version.py"
SCHEMA_DIR = Path("src/pid4cat_model/schema")

MAIN_SCHEMA = """\
id: https://example.org/test
name: test
version: "1.2.3"
prefixes:
  linkml: https://w3id.org/linkml/
  test: https://example.org/test/
default_prefix: test
default_range: string
imports:
  - linkml:types
  - media_types
classes:
  Record:
    description: A record.
    slots:
      - description
      - media_type
slots:
  description:
    description: Free text about the record.
  media_type:
    range: MediaTypes
    required: true
"""

MEDIA_TYPES = """\
id: https://example.org/media_types
name: media_types
prefixes:
  linkml: https://w3id.org/linkml/
default_range: string
imports:
  - linkml:types
enums:
  MediaTypes:
    permissible_values:
      text/csv:
        description: Comma-separated values
"""

REFORMATTED_MAIN_SCHEMA = """\
# The same schema with other formatting, key order and comments
name: test
id: "https://example.org/test"
version: '1.2.3'
default_range: string
default_prefix: test
prefixes: {linkml: "https://w3id.org/linkml/", test: "https://example.org/test/"}
imports: [linkml:types, media_types]
slots:
    media_type: {required: true, range: MediaTypes}
    description:
        description: >-
            Free text about
            the record.
classes:
    Record:
        slots: [description, media_type]
        description: A record.
"""


def git(repo: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-c", "user.name=Test", "-c", "user.email=test@example.org", *args],
        cwd=repo,
        check=True,
        capture_output=True,
    )


def write(repo: Path, name: str, text: str) -> None:
    (repo / SCHEMA_DIR / name).write_text(text, encoding="utf-8")


def edit(repo: Path, name: str, old: str, new: str) -> None:
    text = (repo / SCHEMA_DIR / name).read_text(encoding="utf-8")
    assert old in text
    write(repo, name, text.replace(old, new))


def release(repo: Path, tag: str) -> None:
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "--allow-empty", "-m", tag)
    git(repo, "tag", tag)


def make_repo(tmp_path: Path, tag: str) -> Path:
    (tmp_path / SCHEMA_DIR).mkdir(parents=True)
    write(tmp_path, "pid4cat_model.yaml", MAIN_SCHEMA)
    write(tmp_path, "media_types.yaml", MEDIA_TYPES)
    git(tmp_path, "init", "-q")
    release(tmp_path, tag)
    return tmp_path


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    return make_repo(tmp_path, "v1.2.3.1")


def run_check(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )


def test_reformatted_schema_with_same_version_passes(repo):
    write(repo, "pid4cat_model.yaml", REFORMATTED_MAIN_SCHEMA)
    result = run_check(repo)
    assert result.returncode == 0, result.stderr


def test_documentation_change_with_same_version_passes(repo):
    edit(repo, "pid4cat_model.yaml", "A record.", "A record of a resource.")
    edit(repo, "media_types.yaml", "Comma-separated", "Comma separated")
    result = run_check(repo)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("tag", ["v1.2.3.1", "v1.2.3"])
def test_schema_change_with_same_version_fails(tmp_path, tag):
    repo = make_repo(tmp_path, tag)
    edit(repo, "pid4cat_model.yaml", "required: true", "required: false")
    result = run_check(repo)
    assert result.returncode == 1
    assert "/slots/media_type/required" in result.stderr
    assert tag in result.stderr


def test_change_of_imported_schema_with_same_version_fails(repo):
    edit(
        repo,
        "media_types.yaml",
        "      text/csv:",
        "      text/plain:\n        description: Plain text\n      text/csv:",
    )
    result = run_check(repo)
    assert result.returncode == 1
    assert "/enums/MediaTypes/permissible_values/text/plain" in result.stderr


def test_removed_element_named_like_a_documentation_field_fails(repo):
    edit(repo, "pid4cat_model.yaml", "      - description\n", "")
    edit(
        repo,
        "pid4cat_model.yaml",
        "  description:\n    description: Free text about the record.\n",
        "",
    )
    result = run_check(repo)
    assert result.returncode == 1
    assert "/slots/description" in result.stderr


def test_schema_change_with_new_version_passes(repo):
    edit(repo, "pid4cat_model.yaml", "required: true", "required: false")
    edit(repo, "pid4cat_model.yaml", 'version: "1.2.3"', 'version: "1.3.0"')
    result = run_check(repo)
    assert result.returncode == 0, result.stderr


def test_version_lower_than_release_fails(repo):
    edit(repo, "pid4cat_model.yaml", 'version: "1.2.3"', 'version: "1.2.2"')
    result = run_check(repo)
    assert result.returncode == 1
    assert "1.2.2" in result.stderr


def test_pre_release_is_not_the_baseline(repo):
    edit(repo, "pid4cat_model.yaml", "required: true", "required: false")
    edit(repo, "pid4cat_model.yaml", 'version: "1.2.3"', 'version: "1.3.0"')
    release(repo, "v1.3.0.1rc1")
    edit(repo, "pid4cat_model.yaml", "range: MediaTypes", "range: string")
    result = run_check(repo)
    assert result.returncode == 0, result.stderr
