# -> race_data_raw -> race_data

## -> race_data_raw: to produce `5k_raw.csv` and `10k_raw.csv`
First create `raw.csv` via:
```
python input_data/race_data_raw/05_Sprouty_10k_20220910/get_race_data_raw.py
```
This file includes tables for all race distances and genders.
Manually edit this file to get `5k_raw.csv` and `10k_raw.csv`.

### edits: notes on any manual edits made

## race_data_raw -> race_data: to produce `5k.csv` and `10k.csv`

### edits: notes on any manual edits made

# references
* [https://stackoverflow.com/questions/39757805/using-python-requests-and-beautiful-soup-to-pull-text](https://stackoverflow.com/questions/39757805/using-python-requests-and-beautiful-soup-to-pull-text)