import pytest
from pathlib import Path

import myConfig as XX
from myConfig.inject import Injection
from myConfig.defaults import INI_FILENAME

class Namespace: pass

@pytest.fixture
def CFG():
    xx = Namespace()
    xx.path = Path(__file__).parent/'fixtures/config'
    xx.name = 'foo.bar'
    xx.ini  = xx.path/xx.name/INI_FILENAME
    return xx

@pytest.fixture
def INJ(CFG):
    return Injection(path=CFG.path)

@pytest.fixture
def wrapped(CFG,INJ):
    xx = Namespace()
    xx.ini4name = lambda name: XX.ini4name(name,inj=INJ)
    xx.cfg4name = lambda name: XX.cfg4name(name,inj=INJ)
    return xx

