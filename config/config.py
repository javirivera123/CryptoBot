import json


def load_config():
    try:
        with open('config/config.json') as json_data_file:
            config = json.load(json_data_file)
        print("Config loaded successfully.")
        return config
    except Exception:
        raise Exception("Error when load config")