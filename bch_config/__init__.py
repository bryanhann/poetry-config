#!/usr/bin/env python3

import configparser
from pathlib import Path

from bch_inject import Injection as INJ

from  bch_config.defaults import CONFIG
from  bch_config.defaults import INI_FILENAME

def ini4name( name, inj=INJ(path=CONFIG)):
    """bch_config.ini4name(name) --> path
    Takes a name. Returns the path to its ini file
    """
    return inj.path/name/INI_FILENAME

def cfg4ini(ini):
    """bch_config.cfg4ini(ini) --> cfg
    Takes a name. Returns the path to its ini file
    """
    assert Path(ini).is_file()
    cfg=configparser.ConfigParser()
    cfg.read(ini)
    return cfg

def cfg4name( name, inj=INJ(path=CONFIG)):
    """bch_config.cfg4name(name) --> cfg
    """
    ini = ini4name(name, inj=inj)
    cfg = cfg4ini(ini)
    return cfg
