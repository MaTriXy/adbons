# About adbons
A wrapper for the [Android adb tool](https://developer.android.com/studio/command-line/adb.html). It's just adb on steroids.

## Features
Currently only some basic features are provided. These features should simplify and shorten the required adb commands.

Example workflow to kill an app when multiple devices are connected:
- A default device and app id is set in the config. This information is saved in a `.adbons.yml` file. The file is either stored local (working dir) or global (`~/.adbons/`).
- Execute the kill command. With saved values, the app is just killed with `adbons kill` instead of `adb -s <device> shell am force-stop <app id>`.

## Install
Install the released package from PyPI:
```bash
pip3 install adbons
```

Install from source (developer mode):
```bash
git clone https://github.com/dbaelz/adbons.git
cd adbons
pip install -e .
```

Build a release artifact locally (creates `dist/`):
```bash
python -m pip install --upgrade build
python -m build
```

Upload to TestPyPI or PyPI using `twine`:
```bash
python -m pip install --upgrade twine
# test upload
python -m twine upload --repository testpypi dist/*
# publish
python -m twine upload dist/*
```

Note: this project includes a `pyproject.toml` so it is compatible with modern Python build tools.

## Usage
Once installed, the `adbons` console script is available. Run `adbons --help` for all currently available commands. Individual commands provide help pages as well (e.g. `adbons config --help`).

## Development - Getting started
- (Optional) Create/activate a virtual environment.
- Fork and clone the repository.
- Switch to a feature branch.
- Read the [Click documentation](https://click.palletsprojects.com/) for guidance on writing CLI commands.
- Add your feature/bugfix and run tests.
- Create a pull request.

### Testing
Unit tests are executed with Python's `unittest`:
```bash
python -m unittest discover -v
```

You can also run the project locally by installing it in editable mode (`pip install -e .`) and exercising the `adbons` command.

## License
adbons is licensed under the [BSD License](https://github.com/dbaelz/adbons/blob/master/LICENSE).
