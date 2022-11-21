# -> race_data_raw -> race_data

## -> race_data_raw: to produce `5k_raw.csv` and `10k_raw.csv`
* Download 5k and 10k results from [link to race results](http://www.fiveksport.com/race-results.html) to obtain `10k_raw.pdf` and `5k_raw.pdf`
* These are pdfs, so we will try to parse them with [pypdf2](https://pypdf2.readthedocs.io/en/latest/)
* [PyPDF2 stackoverflow](https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file)
* script to produce `csv`s from pdfs is `08_get_race_data_raw.py`
* ok that didn't go great, better off just copy/paste text and modify to obtain `5k_raw.txt` and `10k_raw.txt`

### edits: notes on any manual edits made

## race_data_raw -> race_data: to produce `5k.csv` and `10k.csv`
From the repository directory run:
```
python input_data/race_data_raw/08_TurkeyTrot_10k_20221120/08_race_data_raw_to_race_data.py
```

### edits: notes on any manual edits made

# references