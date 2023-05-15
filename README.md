In order to run tests after pulling this repo:

1. Open a terminal and run `curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -` this installs Poetry, the package manager used for this project

2. Navigate to where this repo has saved on your machine and run `poetry shell`, this activates the virtual environment for this project

3. Run `poetry install` to install the dependencies (only python 3.11 and pytest 7.1.1)

4. Run `pytest`, or run tests from within your IDE