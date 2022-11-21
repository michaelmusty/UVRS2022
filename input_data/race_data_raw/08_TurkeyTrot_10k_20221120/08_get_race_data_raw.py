"""
From the home directory of the repository run
```
python input_data/race_data_raw/08_TurkeyTrot_10k_20221120/08_get_race_data_raw.py
```
"""

from loguru import logger
from PyPDF2 import PdfReader

path_to_10k_pdf = "input_data/race_data_raw/08_TurkeyTrot_10k_20221120/10k_raw.pdf"
path_to_5k_pdf = "input_data/race_data_raw/08_TurkeyTrot_10k_20221120/5k_raw.pdf"


def _process_path(path: str, which_race: str):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    logger.info(text)


def main():
    _process_path(path_to_10k_pdf, "10k")
    # _process_path(path_to_5k_pdf, "5k")


if __name__ == "__main__":
    main()
