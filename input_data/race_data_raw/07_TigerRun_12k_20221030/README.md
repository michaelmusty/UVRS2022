# -> race_data_raw -> race_data

## -> race_data_raw: to produce `5k_raw.csv` and `12k_raw.csv`
Download csvs from [https://www.lightboxreg.com/iresultslive/?eid=5463](https://www.lightboxreg.com/iresultslive/?eid=5463)
* [5k](https://www.lightboxreg.com/iresultslive/?op=downloadcsv&eid=5463&racename=5K)
* [12k](https://www.lightboxreg.com/iresultslive/?op=downloadcsv&eid=5463&racename=12K)

### edits: notes on any manual edits made
Just rename the files:
```
cp input_data/race_data_raw/07_TigerRun_12k_20221030/Tiger_Run_5k_and_12k_5K.csv input_data/race_data_raw/07_TigerRun_12k_20221030/5k_raw.csv
cp input_data/race_data_raw/07_TigerRun_12k_20221030/Tiger_Run_5k_and_12k_12K.csv input_data/race_data_raw/07_TigerRun_12k_20221030/12k_raw.csv
```

## race_data_raw -> race_data: to produce `5k.csv` and `12k.csv`
From the repository directory run:
```
python input_data/race_data_raw/07_TigerRun_12k_20221030/07_race_data_raw_to_race_data.py
```

### edits: notes on any manual edits made

# references