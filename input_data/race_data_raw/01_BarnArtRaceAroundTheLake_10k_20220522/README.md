# -> race_data_raw -> race_data

## -> race_data_raw
To extract the raw race data these references were helpful:
* [medium article on web scraping](https://medium.com/analytics-vidhya/scraping-tables-from-a-javascript-webpage-using-selenium-beautifulsoup-and-pandas-cbd305ca75fe)
* [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager)

For some reason typing in the url manually works, but using `driver.get(url)` throws an error,
so detailing the steps in `get_race_data_raw.py` here:

First install webdriver
```
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
```

Now, a window should pop up and you need to enter the url of the results page.
I thought the following would work, but it is different somehow:
```
url_5k = "https://runsignup.com/Race/Results/15854#resultSetId-318072;perpage:5000"
url_10k = "https://runsignup.com/Race/Results/15854#resultSetId-318073;perpage:5000"

# pick 5k or 10k
url = url_5k
# url = url_10k

driver.get(url)
```

Now that you have your driver, get your soup
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="lxml")
tables = soup.find_all("table")
```

From your soup you can get a table
```
import pandas as pd  # type: ignore
dfs = pd.read_html(str(tables))
assert len(dfs) == 1
df = dfs[0]
```

And then write the table to `race_data_raw/`
```
df.to_csv("input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/5k_raw.csv")
# df.to_csv("input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/10k_raw.csv")
```

## race_data_raw -> race_data

Once you have `5k_raw.csv` and `10k_raw.csv` in `input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/` directory
you can populate `race_data` via `race_data_raw_to_race_data.py`
```
python input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/race_data_raw_to_race_data.py
```