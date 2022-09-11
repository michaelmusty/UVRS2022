import pandas as pd  # type: ignore
import requests
from bs4 import BeautifulSoup
from loguru import logger

url = "http://802timing.com/results/22results/runresults/9.10.22Sproutyoverall.html"
soup = BeautifulSoup(requests.get(url).content, "html.parser")
tables = soup.find_all("table")

dfs = pd.read_html(str(tables))
assert len(dfs) == 1
df = dfs[0]
logger.info(df)

df.to_csv("input_data/race_data_raw/05_Sprouty_10k_20220910/raw.csv")
