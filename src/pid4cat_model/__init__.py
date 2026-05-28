"""pid4cat-model.

LinkML model for handle-based PIDs for resources in catalysis (pid4cat)
"""

try:
    from pid4cat_model._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
