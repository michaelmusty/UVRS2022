# -> race_data_raw -> race_data

## -> race_data_raw
2022 results are available for download at
[https://www.webscorer.com/race?raceid=282218](https://www.webscorer.com/race?raceid=282218)
resulting in the file
```
input_data/race_data_raw/03_RedWhiteBlue_10k_20220704/'2022 Red White Blue 6.2 and 5K.csv'
```
From this file we manually delete spurious rows to obtain `5k_raw.csv` and `10k_raw.csv`
in the same directory.
Note we also deleted `DNS` and `DNF` rows manually.


### edits

## race_data_raw -> race_data

Once you have `5k_raw.csv` and `10k_raw.csv` in
`input_data/race_data_raw/03_RedWhiteBlue_20220704/` directory
you can populate `race_data` via `03_race_data_raw_to_race_data.py`
```
python input_data/race_data_raw/03_RedWhiteBlue_20220704/03_race_data_raw_to_race_data.py
```