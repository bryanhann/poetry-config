#!/usr/bin/env python3
import pytest
from myConfig import ini4name, cfg4ini, cfg4name


def test_config_is_dir(CFG):
    assert CFG.path.is_dir()


def test_ini4name(CFG,INJ):
    assert ini4name( CFG.name, inj=INJ ) == CFG.ini
    ini =  ini4name( CFG.name, inj=INJ )
    assert ini.is_file()

def test_cfg4ini(CFG,INJ):
    ini =  ini4name( CFG.name, inj=INJ )
    cfg = cfg4ini(ini)
    assert cfg['DEFAULT']['name'] == CFG.name



def test_cfg4name(CFG,INJ):
    cfg = cfg4name(CFG.name, inj=INJ)
    assert cfg['DEFAULT']['name'] == CFG.name



