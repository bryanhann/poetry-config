import sys

import bch_config
import bch_config.usage

ARGS=sys.argv[1:]

def run():
    bch_config.usage.master_usage()

def dump_ini() :
    if not ARGS:
        print(bch_config.usage.DUMP_INI)
        exit()
    ini = bch_config.ini4name(ARGS[0])
    if ini.is_file():
        print(ini.read_text())
