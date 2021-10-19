#!/usr/bin/env python3
from configparser import ConfigParser as CP
from pathlib import Path

CONFIG=Path.home()/'.config'


def ini4name(name,config=CONFIG):
    return config/name/'fig.ini'

def cfg4ini(ini,config=CONFIG):
    assert Path(ini).is_file()
    cfg=CP()
    cfg.read(ini)
    return cfg

def cfg4name(name,config=CONFIG):
    ini = ini4name(name, config)
    cfg = cfg4ini( ini,  config)
    return cfg
