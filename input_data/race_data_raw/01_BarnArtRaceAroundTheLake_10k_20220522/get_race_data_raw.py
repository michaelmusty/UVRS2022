# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# url_5k = "https://runsignup.com/Race/Results/15854#resultSetId-318072;perpage:5000"
# url_10k = "https://runsignup.com/Race/Results/15854#resultSetId-318073;perpage:5000"

# url = url_5k
# # url = url_10k

# driver.get(url)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(driver.page_source, features="lxml")
# tables = soup.find_all("table")

# import pandas as pd  # type: ignore
# dfs = pd.read_html(str(tables))
# assert len(dfs) == 1
# df = dfs[0]

# from loguru import logger
# logger.info(df)

# df.to_csv("input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/5k_raw.csv")
# # df.to_csv("input_data/race_data_raw/01_BarnArtRaceAroundTheLake_10k_20220522/10k_raw.csv")
