import pandas as pd
import json

def load_csv(path):
    return pd.read_csv(path)

def load_json(path):
    with open(path, 'r') as file:
        return pd.json_normalize(json.load(file))

def load_txt(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return pd.DataFrame(lines, columns=['text'])