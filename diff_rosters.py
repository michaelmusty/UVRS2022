"""
diff two UVRC rosters specified as `before` and `after` below:
- inner join on `(fist_name, last_name)`
- list rows present before but not present in join
- list rows present after but not present in join
maybe do the same but join on full rows?

NOTE: there is some duplication of code in `utils.membership`
"""

import glob
import os

import numpy as np
import pandas as pd
from loguru import logger

from utils.membership import PATH_TO_MEMBERSHIP


def get_latest_filename(path_to_dir: str) -> str:
    """returns filename of latest file in a directory with specified path"""
    path = os.path.abspath(path_to_dir)  # absolute path without / at the end
    list_of_filenames = glob.glob(f"{path}/*")
    return max(list_of_filenames, key=os.path.getctime)


def get_second_to_latest_filename(path_to_dir: str) -> str:
    """returns filename of second to latest file in a directory with specified path"""
    path = os.path.abspath(path_to_dir)  # absolute path without / at the end
    list_of_filenames = glob.glob(f"{path}/*")
    logger.info(list_of_filenames)
    list_of_filenames.sort(key=os.path.getctime)
    logger.info(list_of_filenames)
    return list_of_filenames[-2]


def main():
    before_path = get_second_to_latest_filename(PATH_TO_MEMBERSHIP)
    after_path = get_latest_filename(PATH_TO_MEMBERSHIP)
    logger.info(f"before: {before_path}")
    logger.info(f"after : {after_path}")
    before = pd.read_csv(before_path)
    after = pd.read_csv(after_path)
    logger.info(before)
    logger.info(after)


if __name__ == "__main__":
    main()
