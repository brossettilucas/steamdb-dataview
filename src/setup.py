import pandas as pd
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_json_field(field_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = "dicts.json"
    json_path = os.path.join(dir_path, file_name)

    f = open(json_path)
    data = json.load(f)
    return data[field_name][0]


def choose_threshold(mode, field=None, values=None):
    file_name = "steam_trends_data.csv"
    file_path = os.path.join(dir_path, file_name)
    dataCopy = pd.read_csv(file_path)

    main_values = [1501, 3101, 10001, 15001, 30001]

    if mode == 0:
        return dataCopy

    if not (field and values):
        field = "Reviews Total"
        values = main_values

    return dataCopy[dataCopy[field] >= values[(mode - 1)]]
