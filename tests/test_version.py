from importlib.metadata import version

import pid4cat_model


def test_package_version_is_the_installed_distribution_version():
    assert pid4cat_model.__version__ == version("pid4cat-model")


def test_version_tuple_splits_the_package_version_into_ints_and_strs():
    version_tuple = pid4cat_model.__version_tuple__
    assert ".".join(str(part) for part in version_tuple) == (
        pid4cat_model.__version__.replace("+", ".")
    )
    assert all(isinstance(part, int) for part in version_tuple if str(part).isdigit())
