"""script to build dataframe to be consumed by frontend"""

from typing import List

from loguru import logger

from utils.membership import create_people_from_membership_list
from utils.participant import Participant
from utils.participants import get_participants
from utils.person import Person
from utils.race import Race
from utils.races import create_races
from utils.scoring import (
    build_detailed_scorecard,
    build_df,
    build_participation_snapshot,
    build_scorecard,
)


def main():

    # setup
    people: List[Person] = create_people_from_membership_list()
    races: List[Race] = create_races()
    logger.info(
        f"BUILDING participants from {len(people)} people and {len(races)} races"
    )
    participants_for_scoring: List[Participant] = get_participants(
        people=people, races=races, for_scoring=True
    )  # participants in races for scoring
    participants_all: List[Participant] = get_participants(
        people=people, races=races, for_scoring=False
    )  # participants in any eligible race

    # build output_data tables
    logger.info("BUILDING OUTPUT TABLE")
    build_df(participants=participants_for_scoring)  # does not filter top races

    # TODO: build scorecard: raw text output of overall scores for everybody
    # location: output_data/scorecards/scorecard_YYYYMMDDHHMMSS.csv
    # build_scorecard(participants=participants_for_scoring)

    # TODO: build detailed_scorecard: raw text output of all scores (every race) for everybody
    # location: output_data/detailed_scorecards/detailed_scorecard_YYYYMMDDHHMMSS.csv
    # build_detailed_scorecard(participants=participants_for_scoring)

    # TODO: dump participant list
    # build output_data/participation/snapshot_YYYYMMDDHHMMSS.csv
    # build_participation_snapshot(participants=participants_all)


if __name__ == "__main__":
    main()
