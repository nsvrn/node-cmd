import configparser
from pathlib import Path


def get_conf(section=None):
    config = configparser.ConfigParser()
    fpath = Path(__file__).parents[0] / 'settings.conf'
    config.read(fpath)
    conf = config._sections
    if section: conf = conf[section]
    return conf
