# UVRS2022

A dashboard for [UVRS2022](https://uppervalleyrunningclub.org/2022-upper-valley-running-series) scoring.

## Setup notes (for my future self)

First your local machine needs to have python and a fresh `github` repository (which we assume is your working directory for anyting described here).

I like to use [pyenv](https://github.com/pyenv/pyenv),
so at the time of writing I used
```
pyenv install 3.10.4
pyenv global 3.10.4
```
to install the latest python version as my global version.

Next we need a [virtual environment](https://docs.python.org/3/library/venv.html) to install necessary packages and fix dependencies. First create the virtual environment `env`
```
python -m venv env
```
and add `env/` to your `.gitignore`.

To activate your virtual environment use
```
source env/bin/activate
```

Now `pip install` any packages you need
```
pip install isort, loguru, black, mypy, numpy, pandas
```
and when you are satisfied with your environment you can
freeze dependencies
```
pip freeze > requirements.txt
```