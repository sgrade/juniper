import parser
import sys

# Verify Python version
try:
    if not(sys.version_info.major == 2 and sys.version_info.minor == 7) and \
            not(sys.version_info.major == 3):
        raise RuntimeError('Python 2.7 or Python3 required')
except AttributeError:
    raise RuntimeError('Python 2.7 or Python3 required')


__all__ = parser
