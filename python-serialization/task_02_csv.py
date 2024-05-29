#!/usr/bin/python3

'''
    quick doc
'''

import csv
import json


def convert_csv_to_json(filename):
    '''
        quick doc
    '''

    output = []

    try:
        with open(filename, "r", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                output.append(row)
    except Exception:
        return False

    with open("data.json", "w+") as f:
        json.dump(output, f)

    return True
