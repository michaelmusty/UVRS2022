# -> race_data_raw -> race_data

## -> race_data_raw
2022 results are available at
[https://www.runreg.com/RR/a/4217/Under-the-Tree-5K_10K---Results.pdf](https://www.runreg.com/RR/a/4217/Under-the-Tree-5K_10K---Results.pdf)
and the corresponding csv from the race director is
```
input_data/race_data_raw/04_UnderTheTree_10k_20220820/'Under the Tree 5K_10K - sheet1.csv'
```
From this file we manually delete spurious rows and columns to obtain `5k_raw.csv` and `10k_raw.csv`
in the same directory.

### edits
We also made the following manual edits:
* 5k: Robyn Masher -> Robyn Mosher
* 5k: MIke Musty -> Michael Musty
* 10k: Darrell Lasell -> Darrel Lasell

## race_data_raw -> race_data

Once you have `5k_raw.csv` and `10k_raw.csv` in
`input_data/race_data_raw/04_UnderTheTree_10k_20220820/` directory
you can populate `race_data` via `04_race_data_raw_to_race_data.py`
```
python input_data/race_data_raw/04_UnderTheTree_10k_20220820/04_race_data_raw_to_race_data.py
```