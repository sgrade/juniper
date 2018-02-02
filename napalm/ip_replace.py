from __future__ import print_function

import fileinput
import shutil
import sys


def address_replace(ip_address):

    # copy essential template to a tmp directory
    print('Filling template with the IP address:', ip_address)
    tmp_file = '/tmp/base.' + str(ip_address)
    shutil.copyfile('./base.template', tmp_file)

    # writing the IP address instead of the ip_addr place holder
    for line in fileinput.input([tmp_file], inplace=True):
        print(line.replace('ip_addr', ip_address), end='')

    return tmp_file

    print('Done')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide the device\'s IP address')
        sys.exit(1)
    address = sys.argv[1]
    address_replace(address)

