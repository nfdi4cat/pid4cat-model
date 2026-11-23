"""Give docs/overrides priority over plugin-supplied theme dirs.

The mkdocs_pymdownx_material_extras plugin inserts its own theme directory at
position 0 of theme.dirs in its on_config hook, which shadows the user's
custom_dir. This hook runs after plugins and moves custom_dir back to the
front so files under docs/overrides win against the plugin's templates.
"""


def on_config(config):
    custom_dir = config["theme"].custom_dir
    if not custom_dir:
        return config
    dirs = config["theme"].dirs
    if custom_dir in dirs and dirs[0] != custom_dir:
        dirs.remove(custom_dir)
        dirs.insert(0, custom_dir)
    return config
