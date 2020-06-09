'''
File to load the settings
'''
import json
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def load_settings():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    logger.info(" Settings have been loaded")
    return settings

def change_setting(setting, value):
    logger.info(" %s setting is being changed to %s." % (setting, value))
