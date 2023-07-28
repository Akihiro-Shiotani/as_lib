#%%
try:
    import numpy
except ImportError:
    print('AS_SQL bindings requires "numpy" package.')
    print('Install it via command:')
    print('    pip install numpy')
    raise

try:
    import pyodbc
except ImportError:
    print('AS_SQL bindings requires "pyodbc" package.')
    print('Install it via command:')
    print('    pip install pyodbc')
    raise

try:
    import pandas
except ImportError:
    print('AS_SQL bindings requires "pandas" package.')
    print('Install it via command:')
    print('    pip install pandas')
    raise

try:
    import logging
except ImportError:
    print('AS_SQL bindings requires "logging" package.')
    print('Install it via command:')
    print('    pip install logging')
    raise

try:
    import sklearn
except ImportError:
    print('AS_SQL bindings requires "scikit-learn" package.')
    print('Install it via command:')
    print('    pip install scikit-learn')
    raise

try:
    import matplotlib
except ImportError:
    print('AS_SQL bindings requires "matplotlib" package.')
    print('Install it via command:')
    print('    pip install matplotlib')
    raise

import os, glob

__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]