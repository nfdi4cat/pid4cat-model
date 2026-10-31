import subprocess
import sys

import pytest

from pid4cat_model import SCHEMA_VERSION

SCRIPT = "scripts/check_release_tag.py"
MODEL, REVISION, ADDITION = SCHEMA_VERSION.removeprefix("v").split(".")


def run_check(tag: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, SCRIPT, tag], check=False, capture_output=True, text=True
    )


@pytest.mark.parametrize(
    ("tag", "docs_version_and_alias"),
    [
        (f"{SCHEMA_VERSION}.1", f"{SCHEMA_VERSION}.1 {SCHEMA_VERSION}"),
        (f"{SCHEMA_VERSION}.12", f"{SCHEMA_VERSION}.12 {SCHEMA_VERSION}"),
    ],
)
def test_release_is_docs_version_with_schema_version_as_alias(
    tag, docs_version_and_alias
):
    result = run_check(tag)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == docs_version_and_alias


def test_pre_release_is_docs_version_without_schema_version_alias():
    result = run_check(f"{SCHEMA_VERSION}.1rc1")
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == f"{SCHEMA_VERSION}.1rc1"


@pytest.mark.parametrize(
    "tag",
    [
        SCHEMA_VERSION,
        f"{SCHEMA_VERSION}.0",
        f"{SCHEMA_VERSION}rc1",
        f"{SCHEMA_VERSION}.1.1",
        f"{SCHEMA_VERSION}.1b1",
        f"{SCHEMA_VERSION}.1.post1",
        f"v{MODEL}.{REVISION}.{int(ADDITION) + 1}.1",
        f"v{MODEL}.{REVISION}.{ADDITION}1.1",
        f"v{MODEL}.{int(REVISION) + 1}.{ADDITION}.1",
        f"v{MODEL}.{REVISION}.1",
        f"{MODEL}.{REVISION}.{ADDITION}.1",
    ],
)
def test_tag_that_is_not_a_release_of_the_schema_version_fails(tag):
    result = run_check(tag)
    assert result.returncode == 1
    assert result.stdout == ""
    assert SCHEMA_VERSION in result.stderr
