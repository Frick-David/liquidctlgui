'''
File to load the settings
'''
import json

def load_settings():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    print(settings["MinimizeToTray"])
    return settings

def change_setting(setting):
    print(setting)
