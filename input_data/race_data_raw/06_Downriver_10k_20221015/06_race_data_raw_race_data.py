"""
From the home directory of the repository run
```
python input_data/race_data_raw/06_Downriver_10k_20221015/06_race_data_raw_to_race_data.py
```
"""

import csv

import pandas as pd  # type: ignore
from loguru import logger

path_to_10k_raw = "input_data/race_data_raw/06_Downriver_10k_20221015/10k_raw.txt"


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
    with open(path) as f:
        lines: list[str] = f.readlines()
        for row in lines:
            logger.info(f"parsing row: {row}")

            # NAME
            name_with_whitespace = row[:21]  # length of longest name
            name = name_with_whitespace.strip()  # remove leading/trailing whitespace
            s = name.split(" ")
            if len(s) > 2:
                logger.warning(
                    f"name: {name} consists of more than 2 words, might be worth investigating"
                )
            # first = s[0]
            first = " ".join(
                [s[i] for i in range(len(s) - 1)]
            )  # join multiple in first name
            # last = " ".join(
            #     [s[i] for i in range(1, len(s))]
            # )  # join multiple if len(s) > 2
            last = s[-1]
            logger.info(f"parsed first/last as {first} {last}")

            # TIME
            time_with_whitespace = row[28:]  # column where time starts
            time = time_with_whitespace.strip()
            net = _parse_net_time(time)

            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)
    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(f"input_data/race_data/06_Downriver_10k_20221015/{which_race}.csv")


def main():
    _process_path(path_to_10k_raw, "10k")


if __name__ == "__main__":
    main()
