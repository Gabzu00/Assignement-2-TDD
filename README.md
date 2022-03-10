# Assignement-2-TDD

==========================
Get going
--------------------------

### Check version of Python

You have to have Python installed. To check if it's installed and what version you have you 
can write "python --version" in the Command prompt.

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.


### Install Make

1. Install the Windows packet manager Chocolatey: https://chocolatey.org/install

2. Install GNU make using "choco install make" using PowerShell (you might need to run the terminal as admin).

3. Open a new window for Git Bash and check that it works be checking what version you have using make --version.


### Python virtual environment

Install a Python virtual environment and activate it.

install: 
python -m venv .venv

```
# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.


### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

Navigate to the game folder in your terminal: \Assignment 2\Assignement-2-TDD\Assignement-2-TDD\python-template

```
# Do install them
make install

or

python -m pip install -r requirements.txt

# Check what is installed

make installed


### Run the code

The game has to be started by typing this into the terminal:


make play


### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```


### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

### Generate Documentation and UML diagram

We need to install the dot command to help generating the UML pictures from the source code structure when we are using pyreverse. The dot command is part of the package called graphviz and you can install it using your package manager.

If you use Chocolatey package manager, start Powershell as administrator and run the following command: 

choco install graphviz

After the installation is done you can check what version you got with the following command: 

dot -V

# Generate Documentation

make pdoc

or 

make doc

# Generate UML Diagram

make pyreverse