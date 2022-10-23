# -> race_data_raw -> race_data

## -> race_data_raw: to produce `10k_raw.csv`
Copy text from [http://pinnacletiming.us/index.php?n=downriver_rail_run_10k_overall_2022](http://pinnacletiming.us/index.php?n=downriver_rail_run_10k_overall_2022)
to obtain `10k_raw.txt`.

### edits: notes on any manual edits made
Note some multiple-cursor editing is required to get the text in this form.
Also note we replace "Amy Mitchell Gomo" with "Amy Mitchell" to match the UVRS roster.

## race_data_raw -> race_data: to produce `10k.csv`
From the repository directory run:
```
python input_data/race_data_raw/06_Downriver_10k_20221015/06_race_data_raw_to_race_data.py
```

### edits: notes on any manual edits made

# references