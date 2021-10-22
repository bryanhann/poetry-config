import sys
from pathlib import Path

if "MODLIST":
    # MODLIST is a list of modules for which help is printed.
    import bch_config
    MODLIST=[bch_config]

if True:
    # The path to the virtual environment bin directory.
    # This is where the "bch-*" programs are found.
    VENV_BIN=Path(sys.executable).parent

if True:
    PACKAGE_NAME='bch_config'
