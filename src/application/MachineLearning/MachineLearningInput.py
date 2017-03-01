import logging
import numpy as np
import src.application.Domain.League as League
import src.application.Domain.Team as Team


import src.application.MachineLearning.input_train.team_form as team_form_input
import src.application.MachineLearning.input_train.team_home_away_form as team_home_away_form_input
import src.application.MachineLearning.input_train.match_statistics as match_statistics_input
import src.application.MachineLearning.input_train.kekko_input as kekko_input

log = logging.getLogger(__name__)


def get_input_ids():
    return [1, 2, 3]

def get_representations(id):
    if id == 1:
        return team_form_input.get_representations()
    elif id == 2:
        return team_home_away_form_input.get_representations()
    elif id == 3:
        return match_statistics_input.get_representations()
    else:
        return []

def get_input_to_train(id, domain, representation, stage, stages_to_train, season):
    if id == 1:
        log.debug("team form")
        return team_form_input.team_form(domain,
                                         representation,
                                         stage,
                                         stages_to_train=stages_to_train,
                                         season=season)
    if id == 2:
        log.debug("team home away form")
        return team_home_away_form_input.team_home_away_form(domain,
                                                             representation,
                                                             stage,
                                                             stages_to_train=stages_to_train,
                                                             season=season)

    if id == 3:
        log.debug("match statistics")
        return match_statistics_input.match_statistics(domain,
                                                       representation,
                                                       stage,
                                                       stages_to_train=stages_to_train,
                                                       season=season)

    if id == 4:
        log.debug("Kekko input")
        return kekko_input.kekko_input(domain,
                                       representation,
                                       stage,
                                       season,
                                       stages_to_train=stages_to_train)
    else:
        print("The only possible choices are:")
        print("\t1: team_form")
        print("\t2: team_home_away_form")
        print("\t3: match_statistics")
        raise ValueError
