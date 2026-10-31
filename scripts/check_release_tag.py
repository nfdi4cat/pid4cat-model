"""Check a release tag against the schema version and name its docs version.

The first three parts of a release tag are the schema version (see
docs/versioning.md). On success, print the mike version of the release docs,
followed by the schema version as alias. The docs version always has four
parts, so that the schema version can be an alias of the newest release.
A pre-release gets no alias, so that it does not take over the docs of its
schema version. A tag that does not start with the schema version exits with
status 1.

Usage: python scripts/check_release_tag.py v0.4.3.1
"""

import re
import sys

from pid4cat_model import SCHEMA_VERSION


def main(tag: str) -> int:
    match = re.fullmatch(r"v(\d+(?:\.\d+)*)(.*)", tag)
    schema_parts = SCHEMA_VERSION.removeprefix("v").split(".")
    if match is None or match.group(1).split(".")[:3] != schema_parts:
        print(
            f"Tag {tag} does not start with schema version {SCHEMA_VERSION}",
            file=sys.stderr,
        )
        return 1
    release, pre_release = match.groups()
    if pre_release:
        print(tag)
    elif len(release.split(".")) == 3:
        print(f"{tag}.0 {SCHEMA_VERSION}")
    else:
        print(f"{tag} {SCHEMA_VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
