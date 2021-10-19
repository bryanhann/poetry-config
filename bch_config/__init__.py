#!/usr/bin/env python3

import configparser
from pathlib import Path

from bch_inject import Injection as INJ

from  bch_config.defaults import CONFIG
from  bch_config.defaults import INI_FILENAME

def ini4name( name, inj=INJ(path=CONFIG)):
    return inj.path/name/INI_FILENAME

def cfg4ini(ini):
    assert Path(ini).is_file()
    cfg=configparser.ConfigParser()
    cfg.read(ini)
    return cfg

def cfg4name( name, inj=INJ(path=CONFIG)):
    ini = ini4name(name, inj=inj)
    cfg = cfg4ini(ini)
    return cfg
