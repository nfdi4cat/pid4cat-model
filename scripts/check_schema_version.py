"""Check that a changed schema has a new schema version.

Compares the schema with the schema of the newest release tag reachable from
HEAD; pre-releases are not used as baseline. Both are loaded with LinkML and
their imports merged, so formatting, quoting, key order and comments do not
count. Documentation-only fields are ignored as well, so that a documentation
fix can ship as a code-only release; a reviewer bumps the version by hand for
a description change that alters the meaning of an element.

Exits with status 1 if the schema differs while its version equals that of
the baseline release, or if its version is lower than that of the baseline.

Usage (from the repository root): python scripts/check_schema_version.py
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from linkml_runtime import SchemaView
from linkml_runtime.utils.schema_as_dict import schema_as_dict

SCHEMA_DIR = "src/pid4cat_model/schema"
MAIN_SCHEMA = "pid4cat_model.yaml"
DOCUMENTATION_FIELDS = {
    "comments",
    "description",
    "examples",
    "notes",
    "see_also",
    "title",
    "todos",
}
# Fields whose keys are element names, which may equal documentation fields
NAME_KEYED_FIELDS = {
    "annotations",
    "attributes",
    "classes",
    "enums",
    "permissible_values",
    "prefixes",
    "slot_usage",
    "slots",
    "subsets",
    "types",
}


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


def baseline_tag() -> str:
    return git(
        "describe", "--tags", "--abbrev=0", "--match", "v[0-9]*", "--exclude", "*rc*"
    ).strip()


def tag_schema_version(tag: str) -> tuple[int, ...]:
    match = re.match(r"v(\d+)\.(\d+)\.(\d+)", tag)
    if match is None:
        raise ValueError(f"Release tag {tag} does not start with a schema version")
    return tuple(int(part) for part in match.groups())


def load(schema_path: Path) -> tuple[tuple[int, ...], dict]:
    """Return the schema version and the schema without version and docs."""
    schema = schema_as_dict(SchemaView(str(schema_path), merge_imports=True).schema)
    version = tuple(int(part) for part in str(schema.pop("version")).split("."))
    schema.pop("source_file", None)
    return version, without_documentation(schema)


def without_documentation(element: object) -> object:
    if isinstance(element, list):
        return [without_documentation(item) for item in element]
    if not isinstance(element, dict):
        return element
    return {
        key: by_name(value)
        if key in NAME_KEYED_FIELDS
        else without_documentation(value)
        for key, value in element.items()
        if key not in DOCUMENTATION_FIELDS
    }


def by_name(collection: object) -> object:
    if not isinstance(collection, dict):
        return without_documentation(collection)
    return {name: without_documentation(item) for name, item in collection.items()}


def differences(old: object, new: object, path: str = ""):
    if isinstance(old, dict) and isinstance(new, dict):
        for key in sorted(old.keys() | new.keys()):
            yield from differences(old.get(key), new.get(key), f"{path}/{key}")
    elif old != new:
        yield path


def load_tag(tag: str, directory: Path) -> tuple[tuple[int, ...], dict]:
    for name in git("ls-tree", "-r", "--name-only", tag, "--", SCHEMA_DIR).split():
        target = directory / Path(name).relative_to(SCHEMA_DIR)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(
            subprocess.run(
                ["git", "show", f"{tag}:{name}"], check=True, capture_output=True
            ).stdout
        )
    return load(directory / MAIN_SCHEMA)


def main() -> int:
    tag = baseline_tag()
    released = tag_schema_version(tag)
    version, schema = load(Path(SCHEMA_DIR) / MAIN_SCHEMA)
    with tempfile.TemporaryDirectory() as directory:
        _, released_schema = load_tag(tag, Path(directory))
    version_text = ".".join(map(str, version))
    if version < released:
        print(
            f"Schema version {version_text} is lower than that of release {tag}",
            file=sys.stderr,
        )
        return 1
    changed = list(differences(released_schema, schema))
    if changed and version == released:
        print(
            f"The schema differs from that of release {tag} but its version "
            f"{version_text} is unchanged. Differences:",
            *(f"  {path}" for path in changed),
            sep="\n",
            file=sys.stderr,
        )
        return 1
    print(f"Schema version {version_text} is consistent with release {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
