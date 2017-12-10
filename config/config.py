import json
import logging


def load_config():
    logger = logging.getLogger()
    try:
        with open('config/config.json') as json_data_file:
            config = json.load(json_data_file)
        logger.debug("Config loaded successfully.")
        return config
    except Exception as e:
        logger.exception(e)
