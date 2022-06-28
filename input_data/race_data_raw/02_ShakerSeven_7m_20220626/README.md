# -> race_data_raw -> race_data

## -> race_data_raw
2022 results are posted [https://www.gsrs.com/results/4269](https://www.gsrs.com/results/4269)
in `csv` format resulting in the file located at
```
input_data/race_data_raw/02_ShakerSeven_7m_20220626/7m_raw.csv
```

## race_data_raw -> race_data

Once you have `7m_raw.csv` in `input_data/race_data_raw/02_ShakerSeven_7m_20220626/` directory
you can populate `race_data` via `02_race_data_raw_to_race_data.py`
```
python input_data/race_data_raw/02_ShakerSeven_7m_20220626/02_race_data_raw_to_race_data.py
```