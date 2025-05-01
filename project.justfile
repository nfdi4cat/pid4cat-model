## Add your own just recipes here. This is imported by the main justfile.

# Run Python tests and report test coverage
[group('special pid4cat-model')]
coverage:
  uv run python -m coverage run -m pytest
  uv run python -m coverage html
