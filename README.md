# Licensebot
_os license selection guided by a bot >>WORK IN PROGRESS<<_

## Work Progress
- [x] create the decision tree
    - ~~[ ] does [open decision](open-decision.org) help here?~~ no it doesn't
- [x] build the python decision making interface
- [x] create an interactive command-line process
- [x] steamline the process and clean the code
- [ ] build a telegram bot
- [ ] when arrived at a leaf, print whole license contents 
    - is there a website providing them in raw form? would be cumbersome to update them manually if they change

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

TODO
