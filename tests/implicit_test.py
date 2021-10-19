#!/usr/bin/env python3
import pytest
from myConfig import ini4name, cfg4ini, cfg4name


def test_ini4name2(CFG,wrapped):
    assert wrapped.ini4name( CFG.name ) == CFG.ini
    ini =  wrapped.ini4name( CFG.name )
    assert ini.is_file()


def test_cfg4ini2(CFG, wrapped):
    ini =  wrapped.ini4name( CFG.name )
    cfg = cfg4ini(ini)
    assert cfg['DEFAULT']['name'] == CFG.name


def test_cfg4name2(CFG,wrapped):
    cfg = wrapped.cfg4name(CFG.name)
    assert cfg['DEFAULT']['name'] == CFG.name


