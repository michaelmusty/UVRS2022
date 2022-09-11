"""
From the home directory of the repository run
```
python input_data/race_data_raw/05_Sprouty_10k_20220910/05_race_data_raw_to_race_data.py
```
"""

import csv
from typing import Dict, List, Tuple

import pandas as pd  # type: ignore
from loguru import logger

path_to_5k_raw = "input_data/race_data_raw/05_Sprouty_10k_20220910/5k_raw.csv"
path_to_10k_raw = "input_data/race_data_raw/05_Sprouty_10k_20220910/10k_raw.csv"

# these globals are particular to 5k_raw.csv and 10k_raw.csv
NAME_COLUMN_INDEX = 2
NAME_COLUMN_STRING = "Name"
NET_TIME_COLUMN_INDEX = 7


def _parse_net_time(x: str) -> str:
    """
    HH:MM:SS.xx -> HH:MM:SS
    MM:SS.xx -> 00:MM:SS
    also some logic for MM:SS:00 case
    """
    logger.info(f"{x} split on ':' {x.split(':')}")
    if len(x.split(":")) == 3:
        h, m, s = x.split(":")
        if int(h) > 2:  # e.g. 47:52:00, so this probably should be 00:47:52
            return f"00:{h}:{m}"
        else:
            s = s.split(".")[0]
            return f"{h}:{m}:{s}"
    elif len(x.split(":")) == 2:
        m, s = x.split(":")
        s = s.split(".")[0]
        return f"00:{m}:{s}"
    else:
        raise Exception(f"cannot parse net time: {x}")


def _process_path(path: str, which_race: str):
    """
    takes raw race data and formats it to be consumed by the build script
    """
    d: Dict[str, List[str]] = {
        "First Name": [],
        "Last Name": [],
        "Net Time": [],
    }  # this is the thing we need to populate from the raw data
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if (
                row[NAME_COLUMN_INDEX] == NAME_COLUMN_STRING
            ):  # then this row is the header row
                continue
            logger.info(f"parsing row: {row}")
            name = row[NAME_COLUMN_INDEX]
            s = name.split(" ")
            # assert len(s) == 2, f"{name}"
            if len(s) > 2:
                logger.warning(
                    f"name: {name} consists of more than 2 words, might be worth investigating"
                )
            first = s[0]
            # last = s[-1]
            last = " ".join(
                [s[i] for i in range(1, len(s))]
            )  # join multiple if len(s) > 2
            logger.info(f"parsed first/last as {first} {last}")
            net = _parse_net_time(row[NET_TIME_COLUMN_INDEX])
            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)
    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(f"input_data/race_data/05_Sprouty_10k_20220910/{which_race}.csv")


def main():
    _process_path(path_to_5k_raw, "5k")
    _process_path(path_to_10k_raw, "10k")


if __name__ == "__main__":
    main()
