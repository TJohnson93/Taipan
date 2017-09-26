# CONTRIB

To contribute/develop further on this project, the following will need to be
installed:

* Python 3.x
* Pip (Virtual Environment)
* Bower
* Node/NPM

After the above are installed correctly run the following commands to set up the
devlopment environment

## Clone GitHub Project


## Set up Python Virtual Environment

```
pip install --user virtualenv
```

Now that Virtual Environment has been installed, setup project environment.

```
$ cd <cloned-directory>
$ virtualenv venv
New python executable in venv/bin/Python
Installing setuptools, pip............done.
```

Now whenever working on this project, run this command on macOS or Linux

```
$ . venv/bin/activate
```

on Windows:

```
$ venv\scripts\activate
```

To exit the virtual environment, run this command:


```
$ deactivate
```

## Install Python Modules via Pip

Once in your virtual environment run the following command to install the required
Python modules with Pip.

```
$ pip install -r requirements.txt --user
```
