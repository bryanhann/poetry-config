import bch_config.constants as __C

def help4mod(mod):
    """Yield all appropriate docstrings in given module.
    """
    for name in dir(mod):
        doc=getattr(mod,name).__doc__
        if doc and doc.startswith( 'bch_config.' ):
            yield doc.strip()

def bin_commands():
    """Yield paths to all appropriate commands in venv's bin.
    """
    prefix = __C.PACKAGE_NAME.replace('_', '-')
    for path in __C.VENV_BIN.glob('*'):
        if path.name.startswith(prefix):
            yield path

