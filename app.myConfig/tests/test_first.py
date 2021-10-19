#!/usr/bin/env python3

from myConfig import ini4name, cfg4ini, cfg4name

def test_config_is_dir(CFG):
    assert CFG.path.is_dir()

def test_ini4name(CFG):
    assert ini4name( CFG.name, config=CFG.path ) == CFG.ini
    ini =  ini4name( CFG.name, config=CFG.path )
    assert ini.is_file()

def test_cfg4ini(CFG):
    ini =  ini4name( CFG.name, config=CFG.path )
    cfg = cfg4ini(ini, config=CFG.path)
    assert cfg['DEFAULT']['name'] == CFG.name

def test_cfg4name(CFG):
    cfg = cfg4name(CFG.name, config=CFG.path)
    assert cfg['DEFAULT']['name'] == CFG.name
