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
pip install isort loguru black mypy numpy pandas bs4 requests selenium lxml webdriver-manager dash plotly
```
and when you are satisfied with your environment you can
freeze dependencies
```
pip freeze > requirements.txt
```

Note that we can format python code, imports, and mypy type checking using
```
isort --skip-gitignore . && black . && mypy .
```

## github, deployment, environment, and tests (eventually)

* `build.py` script to build `output_data` from `input_data`
* `app.py` contains the frontend logic for the Dash app
* `requirements.txt` contains the dependencies for the virtualenv
* `Procfile` is necessary for Heroku deployment
* `.github/workflows/main.yml` controls github action to deploy to Heroku on a push

Note that deployment on a push requires a heroku project, creating a repository secret with the heroku API key, etc.
The steps are detailed in the references.

## python code
### `utils/` directory with the backend python code
### classes
* `Person`: a person in the membership list
* `Race`: a UVRS race
* `Racer`: a racer in a UVRS race
* `Participant`: a person that has been matched to at least one racer

## data

### `input_data/`
* `rosters_private/` contains local snapshots of the UVRC membership list (not committed for privacy)
* `race_data/` directory contains the tabular data for the UVRS races, directories are named with race dates of the form YYYYMMDD
* `race_data_raw/` directory contains raw race data which we process (sometimes by hand if we must) before writing to `race_data/`. Additional documentation for each race will also live here.

### `output_data/`
* `tables/df_YYYYMMDDHHMMSS.csv` snapshot scores table to be used by `app.py` including all races
* `participation/snapshot_YYYYMMDDHHMMSS.csv` snapshot of all matched UVRS participants for a given membership snapshot (with private data excluded for privacy) with columns `Individual`, `NumRaces`

## references
* [https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index](https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index)
* [https://dash.plotly.com/basic-callbacks](https://dash.plotly.com/basic-callbacks)
* [https://dash.plotly.com/deployment](https://dash.plotly.com/deployment)
* [https://github.com/marketplace/actions/deploy-to-heroku](https://github.com/marketplace/actions/deploy-to-heroku)
* [https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code](https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code)
* [https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)
* [https://developers.google.com/sheets/api/quickstart/python](https://developers.google.com/sheets/api/quickstart/python)
* [word2vec](https://radimrehurek.com/gensim/models/word2vec.html)
* [https://github.com/plotly/dash-pivottable](https://github.com/plotly/dash-pivottable)
* [https://bergvca.github.io/2017/10/14/super-fast-string-matching.html](https://bergvca.github.io/2017/10/14/super-fast-string-matching.html)
* [https://bergvca.github.io/2020/01/02/string-grouper.html](https://bergvca.github.io/2020/01/02/string-grouper.html)
* [https://github.com/Bergvca/string_grouper](https://github.com/Bergvca/string_grouper)
* [https://stackoverflow.com/questions/33021874/heroku-gunicorn-not-working-bash-gunicorn-command-not-found](https://stackoverflow.com/questions/33021874/heroku-gunicorn-not-working-bash-gunicorn-command-not-found)