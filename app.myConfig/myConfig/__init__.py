#!/usr/bin/env python3

import configparser
from pathlib import Path

import myConfig.defaults as DD

def ini4name(name,config=DD.CONFIG):
    return config/name/DD.INI_FILENAME

def cfg4ini(ini,config=DD.CONFIG):
    assert Path(ini).is_file()
    cfg=configparser.ConfigParser()
    cfg.read(ini)
    return cfg

def cfg4name(name,config=DD.CONFIG):
    ini = ini4name(name, config)
    cfg = cfg4ini(ini, config)
    return cfg
