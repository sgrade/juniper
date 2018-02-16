from __future__ import print_function

import fileinput
import shutil
import sys
import os


def address_replace(ip_address):
    """
    Creates base device config from base template:
    replaces the IP_ADDR in the template with the device's IP address
    :param ip_address: device IP
    :return: base config file name
    """

    work_dir = os.getcwd()
    base_template = work_dir+'/parser_configs/base_template'

    # copy essential template to a tmp directory
    print('Filling template with the IP address:', ip_address)
    tmp_file = '/tmp/base.' + str(ip_address)
    shutil.copyfile(base_template, tmp_file)

    # writing the IP address instead of the ip_addr place holder
    for line in fileinput.input([tmp_file], inplace=True):
        print(line.replace('IP_ADDR', ip_address), end='')

    return tmp_file


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide the device\'s IP address')
        sys.exit(1)
    address = sys.argv[1]
    address_replace(address)

