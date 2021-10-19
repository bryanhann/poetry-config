#!/usr/bin/env python3

from myConfig import ini4name, cfg4ini, cfg4name

NAME='foo.bar'

def test_config_is_dir(CONFIG):
    assert CONFIG.is_dir()

def test_ini4name(CONFIG):
    ini =  ini4name( NAME, config=CONFIG )
    assert ini.is_file()

def test_cfg4ini(CONFIG):
    ini =  ini4name( NAME, config=CONFIG )
    cfg = cfg4ini(ini, config=CONFIG)
    assert cfg['DEFAULT']['name'] == NAME

def test_cfg4name(CONFIG):
    cfg = cfg4name(NAME, config=CONFIG)
    assert cfg['DEFAULT']['name'] == NAME
