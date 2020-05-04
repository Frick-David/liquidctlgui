'''
File to load the settings
'''
import json

with open('settings.json', 'r') as f:
    settings = json.load(f)
