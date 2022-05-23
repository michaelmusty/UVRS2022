"""Utilities for computing scores from a list of participant objects"""

import datetime
from typing import Dict, List, Tuple

import pandas as pd  # type: ignore
from loguru import logger

from utils.participant import Participant
from utils.race import Race
from utils.racer import Racer


def build_df(participants: List[Participant]):
    """construct df for the frontend to consume and write to output_data/tables/df_timestamp.csv"""

    # initialize columns of table we want to construct
    col_individual: List[str] = []  # column "Individual" with name of a participant
    col_score: List[
        int
    ] = []  # column "Score" with an individual's score for a given race
    col_race: List[str] = []  # column "Race" with name of a race
    col_age_group: List[
        str
    ] = []  # column "Age Group" with the age group of participant

    # each pair (p,race) corresponds to a row of df
    for p in participants:
        for race in p.races:
            i, s, r, a = get_df_row(participant=p, participants=participants, race=race)
            col_individual.append(i)
            col_score.append(s)
            col_race.append(r)
            col_age_group.append(a)
            logger.info(f"data row: {i}, {s}, {r}, {a}")

    # build dict and then df
    df = pd.DataFrame(
        {
            "Individual": col_individual,
            "Score": col_score,
            "Race": col_race,
            "Age Group": col_age_group,
        }
    )

    # write df to file
    dt_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(f"output_data/tables/df_{dt_str}.csv")

    return df


def get_df_row(
    participant: Participant, participants: List[Participant], race: Race
) -> Tuple[str, int, str, str]:
    """
    returns a 4-tuple (individual, score, race, age_group) for the participant in given race
    the score is computed for participant relative to the other participants
    """
    assert (
        race in participant.races
    )  # race must be a race that participant participated in

    # p_with_faster_time is a list of participants with faster time than given participant
    # p_with_slower_time is a list of participants with slower time than given participant
    # p_with_equal_time is a list of participants with the same race time as given participant
    p_with_faster_time: List[Participant] = []
    p_with_slower_time: List[Participant] = []
    p_with_equal_time: List[Participant] = []

    # precompute age group and race time for fixed participant
    participant_age_group: str = participant.age_group()  # age group to compare against
    participant_time = participant.get_corresponding_racer(
        race=race
    ).get_net_time()  # race time to compare against

    # loop over participants to compare against
    for p in participants:
        if (
            race in p.races
        ):  # participant p must have run given race otherwise we don't care
            if participant_age_group == p.age_group():  # check that age groups match
                # now compare race times between participant (computed outside the loop) and p (computed below)
                p_time = p.get_corresponding_racer(race=race).get_net_time()
                if p_time == participant_time:  # participant tied with p
                    p_with_equal_time.append(p)
                elif p_time < participant_time:  # p had a faster time than participant
                    p_with_faster_time.append(p)
                elif p_time > participant_time:  # p had a slower time than participant
                    p_with_slower_time.append(p)

    # now use p_with_faster_time to compute a score
    if len(p_with_faster_time) == 0:  # then participant has 1st fastest time
        score = 100
    elif len(p_with_faster_time) == 1:  # then participant has 2nd fastest time
        score: int = 90
    elif len(p_with_faster_time) == 2:  # then participant has 3rd fastest time
        score: int = 82
    elif len(p_with_faster_time) == 3:  # then participant has 4th fastest time
        score: int = 75
    elif len(p_with_faster_time) == 4:  # then participant has 5th fastest time
        score: int = 69
    elif len(p_with_faster_time) == 5:  # then participant has 6th fastest time
        score: int = 63
    elif len(p_with_faster_time) == 6:  # then participant has 7th fastest time
        score: int = 58
    elif len(p_with_faster_time) == 7:  # then participant has 8th fastest time
        score: int = 53
    elif len(p_with_faster_time) == 8:  # then participant has 9th fastest time
        score: int = 49
    elif len(p_with_faster_time) == 9:  # then participant has 10th fastest time
        score: int = 45
    elif len(p_with_faster_time) == 10:  # then participant has 11th fastest time
        score: int = 41
    elif len(p_with_faster_time) == 11:  # then participant has 12th fastest time
        score: int = 37
    elif len(p_with_faster_time) == 12:  # then participant has 13th fastest time
        score: int = 34
    elif len(p_with_faster_time) == 13:  # then participant has 14th fastest time
        score: int = 31
    elif len(p_with_faster_time) == 14:  # then participant has 15th fastest time
        score: int = 28
    elif len(p_with_faster_time) > 14:  # then participant placed 16th or higher
        score: int = 25

    # return 4-tuple
    return (
        participant.person.name(),
        score,
        race.get_full_name(),
        participant_age_group,
    )


def build_filtered_df(participants: List[Participant], N: int):
    """same as build_df but filters top N races"""

    # initialize columns of table we want to construct
    col_individual: List[str] = []  # column "Individual" with name of a participant
    col_score: List[
        int
    ] = []  # column "Score" with an individual's score for a given race
    col_race: List[str] = []  # column "Race" with name of a race
    col_age_group: List[
        str
    ] = []  # column "Age Group" with the age group of participant

    # each pair (p,race) corresponds to a row of df
    for p in participants:
        col_i: List[
            str
        ] = []  # these are partial columns for rows corresponding to p only
        col_s: List[int] = []
        col_r: List[str] = []
        col_a: List[str] = []
        for race in p.races:
            i, s, r, a = get_df_row(participant=p, participants=participants, race=race)
            col_i.append(i)
            col_s.append(s)
            col_r.append(r)
            col_a.append(a)
            logger.info(f"data row: {i}, {s}, {r}, {a}")
        # now filter to length N by popping rows with minimum score (col_s has scores) until length <= N
        while len(col_s) > N:
            min_ind = col_s.index(
                min(col_s)
            )  # the index of the (first) minimum score in the list col_s
            col_i.pop(min_ind)
            col_s.pop(min_ind)
            col_r.pop(min_ind)
            col_a.pop(min_ind)
        assert len(col_i) <= N
        assert len(col_s) <= N
        assert len(col_r) <= N
        assert len(col_a) <= N
        assert len(col_i) == len(col_s)
        assert len(col_i) == len(col_r)
        assert len(col_i) == len(col_a)
        # now concatenate lists
        col_individual += col_i
        col_score += col_s
        col_race += col_r
        col_age_group += col_a

    # build dict and then df
    df = pd.DataFrame(
        {
            "Individual": col_individual,
            "Score": col_score,
            "Race": col_race,
            "Age Group": col_age_group,
        }
    )

    # write df to file
    dt_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(f"output_data/filtered_tables/df_{dt_str}.csv")

    return df


# TODO
def build_participation_snapshot(participants: List[Participant]):
    pass
