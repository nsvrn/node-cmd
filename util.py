import configparser, subprocess, shutil
from pathlib import Path

CONF_PATH = Path(__file__).parent / 'settings.conf'
SAMPLE_CONF_PATH = Path(__file__).parent / 'settings.conf.sample'

def get_conf(section=None):
    if CONF_PATH.exists():
        config = configparser.ConfigParser()
        config.read(CONF_PATH)
        conf = config._sections
        if section: conf = conf[section]
        return conf
    else:
        load_settings()

def load_settings():
    if not CONF_PATH.exists():
        shutil.copy(SAMPLE_CONF_PATH, CONF_PATH)
    subprocess.call(['vim', CONF_PATH])