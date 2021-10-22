import sys
from pathlib import Path
import textwrap
import bch_config.constants as __C
import bch_config.util as __U
PROG=Path(sys.argv[0]).name

DUMP_INI=f"""
USAGE:\n\t{PROG} NAME\n
DESCRIPTION:\n\tDump the ini file associated with NAME\n
EXAMPLE:\n\t{PROG} foo.bar\n\n\tCat the file ~/.config/foo.bar/fig.ini
"""



def master_usage_commands():
    commands = __U.bin_commands()
    if commands:
        print('COMMANDS:')
        for path in commands:
            print(f"\t{path.name}")
        print()

def master_usage_library():
    print( 'LIBRARY:' )
    for mod in __C.MODLIST:
        for block in __U.help4mod(mod):
            print( textwrap.indent(block,'\t') + '\n' )

def master_usage():
    """Print master help for the package.
    """
    print( f'The {__C.PACKAGE_NAME.upper()} module.\n')
    master_usage_commands()
    master_usage_library()

