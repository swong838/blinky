import os
from yaml import load, Loader

config_file = os.path.abspath('./blinky/lib/config.yml')

with open(config_file, 'r') as stream:
    config_data = load(stream)


class Constants():

    RATE = config_data['rate']
    MAX = int(255 * ((config_data['max_brightness'] % 100) * .01))
    PINS = {
        'RED': config_data['pins']['RED'],
        'GREEN': config_data['pins']['GREEN'],
        'BLUE': config_data['pins']['BLUE']
    }
