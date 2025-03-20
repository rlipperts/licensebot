# python_package_template
_Default files and structure for python package repositories (aimed at personal use)_

## installation
There are no PyPI releases. Neither are they planned.

### setup project environment for development
To setup this project to develop in it:
- Install python 3.12 and [poetry](https://python-poetry.org/docs/)
- Adjust template
    - edit this readme
    - change your package-name `src/package_name` and module name `src/package_name/module_name.py`
    - change the name of the test under `tests/test_module_name.py`
    - adjust the project data in the `pyproject.toml`
        - change the name of your project
        - adjust author, version, description
        - update the path to your code in the `packages` table
    - remove the template workflow under `.github/workflows/template_tests.yml`
- Setup poetry environment
    - `poetry lock`
    - `poetry install --with dev`
- Install the ruff pre-commit hooks
    - `poetry run pre-commit install`

## usage

Write a more or less detailed description on how to use your package!
