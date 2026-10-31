"""Check a release tag against the schema version and name its docs version.

A release tag is the schema version followed by a release number from 1, for
example v0.4.3.1 (see docs/versioning.md). On success, print the tag as mike
version of the release docs, followed by the schema version as alias. A
pre-release (suffix "rc" and a number) gets no alias, so that it does not take
over the docs of its schema version. Any other tag exits with status 1.

Usage: python scripts/check_release_tag.py v0.4.3.1
"""

import re
import sys

from pid4cat_model import SCHEMA_VERSION


def main(tag: str) -> int:
    match = re.fullmatch(r"(v\d+\.\d+\.\d+)\.([1-9]\d*)(rc\d+)?", tag)
    if match is None or match.group(1) != SCHEMA_VERSION:
        print(
            f"Tag {tag} is not schema version {SCHEMA_VERSION} followed by a "
            "release number from 1",
            file=sys.stderr,
        )
        return 1
    if match.group(3):
        print(tag)
    else:
        print(f"{tag} {SCHEMA_VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
