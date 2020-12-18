# Description of installation procedure for pipenv

Pipenv is a dependency and virtual environment management tool
recommended in the [Python packaging documentation](https://packaging.python.org/tutorials/managing-dependencies/). This document describes the installation
of pipenv on the Window, Macos and Linux operating systems.

## Install instructions

The recommended installation procedure varies slightly depending on the system.
operating system you are using. You will find below simple installation procedures
 for each system. They summarize the instructions we can read on [the official documentation](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

### Installing pipenv on windows

To install pipenv on windows, the only prerequisite is to have a working
installation of python 3 and pip. The installation of the pipenv tool can be achieved with the following command:

```
$ pip install pipenv
```

You can check the correct installation of pipenv by running the command
`pipenv --version`. Once pipenv is installed and functional on your system, do not hesitate to have a look at the "Benefits and Usage" section below. Happipenv!

### Installing pipenv on macos

To install pipenv on macos, the recommended approach is to [use homebrew](https://brew.sh/) if you are already a user. It's a must-use for
development under macos. Installation of pipenv using homebrew is quite simple:

```
$ brew install pipenv
```

For those of you who do not use homebrew (rare among devs under macos), 
it is of course also possible to install pipenv using pip3 and the following command:

```
$ pip3 install pipenv
```

You can check the correct installation of pipenv by running the command
`pipenv --version`. Once pipenv is installed and functional on your system, do not hesitate to have a look at the "Benefits and Usage" section below. Happipenv!

## Installing pipenv on Fedora > 28

On Fedora, it is possible to directly install pipenv using dnf since version 28 of the system. Here is the installation command:

```
sudo dnf install pipenv
```

You can also use a classical installation using pip3. If this is your wish, please refer to the next section.

You can check the correct installation of pipenv by running the command
`pipenv --version`. Once pipenv is installed and functional on your system, do not hesitate to have a look at the "Benefits and Usage" section below. Happipenv!

### Installing pipenv on Debian, Ubuntu and any linux

To install pipenv on Debian, Ubuntu and any other linux, the only prerequisite is to have a working
installation of python3 and pip3. Installing requires the following command:

```
$ pip3 install --user pipenv
```

This command will install pipenv into the `$HOME/.local/bin` directory. Check
that this directory is in the PATH. If necessary, you can add the command
`export PATH="$HOME/.local/bin:$PATH"` in the `$HOME/.profile` file.

You can check the correct installation of pipenv by running the command
`pipenv --version`. Once pipenv is installed and functional on your system, do not hesitate to have a look at the "Benefits and Usage" section below. Happipenv!

## Benefits and Usage
The advantages of pipenv compared to an explicit use of the classic combo
venv+pip are the following:

- `pipenv install` automatically creates a virtual environment when you install your dependencies, a library or a tool. You cannot install by mistake such dependencies globally.
- `pipenv install` automatically adds each dependency installed in
a Pipfile and a Pipfile.lock files. Both files can 
be added to your commits and shared between all members of your
development. These files play the role of a requirements.txt file with
the advantage of being automatically generated and updated. These files also separate efficiently the 
direct and indirect dependencies in two files. You only see your direct dependencies in Pipfile.
- `pipenv shell` allows to activate the virtual environment with the same command
on all operating systems. No more need to detail different commands for windows and macos/linux. The command `exit` then allows to leave this virtual environment.
- `pipenv run <command>` allows to run a command within a virtual environment
without having to activate it explicitely.
- `pipenv install` does not create its virtual environment in the current directory which is generally considered a bad practice. This prevents you from sending it to github by mistake. You
can know the path to this virtual environment using the command
`pipenv --venv` and destroy it with the command `pipenv --rm`.
