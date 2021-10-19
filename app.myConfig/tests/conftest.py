import pytest
from pathlib import Path

import myConfig.defaults as DD

class Namespace: pass

@pytest.fixture
def CFG():
    xx = Namespace()
    xx.path = Path(__file__).parent/'fixtures/config'
    xx.name = 'foo.bar'
    xx.ini  = xx.path/xx.name/DD.INI_FILENAME
    assert xx.ini.is_file()
    return xx
