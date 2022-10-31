"""
From the home directory of the repository run
```
python input_data/race_data_raw/07_TigerRun_12k_20221030/07_race_data_raw_to_race_data.py
```
"""

import csv

import pandas as pd  # type: ignore
from loguru import logger

path_to_5k_raw = "input_data/race_data_raw/07_TigerRun_12k_20221030/5k_raw.csv"
path_to_12k_raw = "input_data/race_data_raw/07_TigerRun_12k_20221030/12k_raw.csv"


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

    d: dict[str, list[str]] = {
        "First Name": [],
        "Last Name": [],
        "Net Time": [],
    }  # this is the thing we need to populate from the raw data

    with open(path, newline="") as csvfile:

        reader = csv.reader(csvfile, delimiter=",")

        for row in reader:

            # check for header row
            if row[0] == "Place":
                continue

            logger.info(f"parsing row: {row}")

            # NAME
            first = row[1].strip()
            last = row[2].strip()
            name = first + " " + last
            if len(name.split(" ")) > 2:
                logger.warning(
                    f"name: {name} consists of more than 2 words, might be worth investigating row \n{row}"
                )
            logger.info(f"parsed first/last as {first} {last}")

            # TIME
            time_with_whitespace = row[6]
            time = time_with_whitespace.strip()
            net = _parse_net_time(time)

            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)

    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(f"input_data/race_data/07_TigerRun_12k_20221030/{which_race}.csv")


def main():
    _process_path(path_to_5k_raw, "5k")
    _process_path(path_to_12k_raw, "12k")


if __name__ == "__main__":
    main()
