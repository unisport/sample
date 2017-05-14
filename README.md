# Unisport Code Challenge
## Installation
Working Ubuntu installation process

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
