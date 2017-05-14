# Unisport Code Challenge
## Installation
Working Ubuntu installation process

First, check if da_DK.UTF-8 locale is already in the system with:
```bash
$ locale -a
```
If it is not in the list, do:
```bash
$ sudo locale-gen da_DK.UTF-8
$ sudo update-locale
```

Once the locale is installed on the system:
```bash
$ sudo pip install virtualenv
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=hello.py

```

## Usage
```bash
$ . venv/bin/activate (Only if it was deactivated before)
$ flask run

```


## Testing

```bash
$ python -m unittest discover
```

## Check the code follows PEP 8 convention
```bash
$ pep8 *.py
```
