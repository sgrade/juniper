import sys
from loader.loader import Loader


"""
Allows using script with CLI arguments

Usage:
python loader.py lab_number [hostname]
1) If only lab_number provided, replaces all configs for all devices in the lab
2) If lab_number and hostname provided, replaces config for one device
"""
if len(sys.argv) == 2:
    _lab_number = sys.argv[1]
    x = Loader()
    x.load_all_configs(_lab_number)
elif len(sys.argv) == 3:
    _lab_number = sys.argv[1]
    _host = sys.argv[2]
    x = Loader()
    x.load_base_config(_host)
    x.load_lab_config(_lab_number, _host)
else:
    print('Please provide CLI arguments: lab number OR lab number and hostname')
    print('allowed lab numbers: 1, 2, ... 11')
    print('allowed host names: r1, r2, r3, r4, r5, vrdevice')
    sys.exit(1)
