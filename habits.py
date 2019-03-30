import json


AVG_CAL = 2500


def check_habits():
    with open('historical/calories.json') as json_data:
        eat = json.load(json_data)

    tot_cal = 0
    for key, value in eat.items():
        tot_cal += value

    # Simulating that the calories.json file is carrying data about two days
    if tot_cal/2 > AVG_CAL:
        return True

    return False
