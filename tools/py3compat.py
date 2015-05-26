import sys
import warnings
PY3 = sys.version > "3"

if PY3:
    warnings.warn("Python 3 Support is HIGHLY EXPERIMENTAL")

toStr = lambda a: a if type(a) == "str" else a.decode("UTF-8")
toBytes = lambda a: a if type(a) == "bytes" else a.encode()
