"""Utilities to create participants from people"""

import itertools
from typing import Dict, List, Optional, Tuple

from loguru import logger

from utils.participant import Participant
from utils.person import Person
from utils.race import Race
from utils.racer import Racer


def get_participants(
    people: List[Person], races: List[Race], for_scoring: bool
) -> List[Participant]:
    """compute list of participants by checking if each person is a participant"""
    participants: List[Participant] = []
    for person in people:
        b, p = is_participant(
            person=person, races=races, for_scoring=for_scoring
        )  # p is a participant
        if b:
            assert p
            if for_scoring:
                logger.info(
                    f"{person.name()} is a participant (only including races for scoring)\n{person.name()} races: {[x.get_full_name() for x in p.races]}\n{person.name()} racer: {[x.get_name() for x in p.racers]}"
                )
            else:
                logger.info(
                    f"{person.name()} is a participant (including all races and distances)\n{person.name()} races: {[x.get_full_name() for x in p.races]}\n{person.name()} racer: {[x.get_name() for x in p.racers]}"
                )
            # logger.info(f"{person.name()} races: {[x.get_full_name() for x in p.races]}")
            # logger.info(f"{person.name()} racer: {[x.get_name() for x in p.racers]}")
            participants.append(p)
        else:
            logger.info(f"{person.name()} is not a participant")
    return participants


def is_participant(
    person: Person, races: List[Race], for_scoring: bool
) -> Tuple[bool, Optional[Participant]]:
    """determine if person is a participant in any of races and if so construct participant"""

    races_participated_in: List[Race] = []
    corresponding_racers: List[Racer] = []
    for race in races:
        b, p = is_participant_in_race(person=person, race=race, for_scoring=for_scoring)
        if b:
            assert p
            races_participated_in.append(race)
            corresponding_racers.append(p)

    if len(races_participated_in) > 0:
        assert len(races_participated_in) == len(corresponding_racers)
        participant = Participant(
            person=person,
            races=races_participated_in,
            racers=corresponding_racers,
        )
        return (True, participant)
    else:
        return (False, None)


def is_participant_in_race(
    person: Person, race: Race, for_scoring: bool
) -> Tuple[bool, Optional[Racer]]:
    """true if person is particpant in race and the corresponding racer is also returned"""
    if for_scoring:
        racers = race.get_racers()[
            race.get_race_distance_used_for_scoring()
        ]  # here just use race distance that we want for scoring
    else:
        racers_d: Dict[
            str, List[Racer]
        ] = race.get_racers()  # keys are all race distances
        racers: List[Racer] = list(
            itertools.chain.from_iterable([racers_d[k] for k in racers_d.keys()])
        )

    matched_racers: List[Racer] = []
    for racer in racers:
        if does_person_match_racer(person=person, racer=racer):
            matched_racers.append(racer)

    if len(matched_racers) == 0:
        return (False, None)
    elif len(matched_racers) == 1:
        return (True, matched_racers[0])
    else:
        raise Exception(
            f"""
            Number of matched racers = {len(matched_racers)} which should not occur:\n
            {person.name()} matched with\n
            {[x.get_name() for x in matched_racers]}
            """
        )


# TODO: add other match algorithms
def does_person_match_racer(
    person: Person, racer: Racer, match_algorithm: str = "exact"
) -> bool:
    """true if person matches racer based on names only"""
    assert match_algorithm == "exact"
    return person.name().casefold() == racer.get_name().casefold()
