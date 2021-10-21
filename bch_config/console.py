import sys
from pathlib import Path

import bch_config as XX

BASEPROG='bch_config'
PROG=Path(sys.argv[0]).name

USAGE_dump_ini=f"""
USAGE:\n\t{PROG} NAME\n
DESCRIPTION:\n\tDump the ini file associated with NAME\n
EXAMPLE:\n\t{PROG} foo.bar\n\n\tCat the file ~/.config/foo.bar/fig.ini
""".strip()

def run():
    usage()

def usage():
    print( f'The {BASEPROG.upper()} module.\n\nCOMMANDS:')
    for path in Path(sys.executable).parent.glob('*'):
        if path.name.startswith(BASEPROG.replace('_', '-')):
            print(f"\t{path.name}")

def dump_ini() :
    len(sys.argv)==1 and exit(print(USAGE_dump_ini))
    ini=Path(XX.ini4name(sys.argv[1]))
    ini.is_file() and print(ini.read_text())
