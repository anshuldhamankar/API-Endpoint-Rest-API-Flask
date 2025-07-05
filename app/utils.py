import json
import os

def load_wimbledon_data():
    file_path = os.path.join(os.path.dirname(__file__), 'wimbledon.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
