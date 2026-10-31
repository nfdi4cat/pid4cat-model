import re
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pid4cat-model")
except PackageNotFoundError:
    # package not installed
    __version__ = "0.0.0"

# tuple[int | str, ...] like the _version.py files written by setuptools-scm
__version_tuple__ = tuple(
    int(part) if part.isdigit() else part for part in re.split(r"[.+]", __version__)
)
