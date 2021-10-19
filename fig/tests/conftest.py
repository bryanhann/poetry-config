import pytest

from pathlib import Path
@pytest.fixture
def CONFIG():
    return Path(__file__).parent/'fixtures/config'
