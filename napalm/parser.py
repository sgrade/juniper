from __future__ import print_function

import os
import sys
import yaml
from config_replace import config_replace
from ip_replace import address_replace


def main(lab_number):

    cfg = parse_ip_addresses('ip-addresses.yml')

    for router, ip in cfg.items():
        print('')
        print('======================')
        print('Starting with', router, 'using IP', ip)
        lab_config = find_config(lab_number, router)
        base_config = address_replace(ip)
        config_replace(ip, lab_config, base_config)
        print('Finished with', router, 'using IP', ip)
        print('======================')

    print('')
    print('Done!')
    print('')


def parse_ip_addresses(file):
    """
    Creates a dictionary with router name and IP from config file
    :rtype: dict
    """
    with open(file) as ymlfile:
        cfg = yaml.load(ymlfile)
        return cfg


def find_config(lab, router):
    """
    Looking for the router's config in the lab directory
    :rtype: string
    """

    # Lab number should be with a leading zero
    if int(lab) < 10:
        lab = str(0) + str(lab)
    lab_dir = "/home/roman/JS-topologies/JNCIE-SP_Bootcamp_12a_L" + lab + "/configset"

    # Getting all filenames in the lab directory
    dir_list = os.listdir(lab_dir)

    # Looking for a filename, where first two letters are the same as the router name
    # As VR-device-related filenames can be in different registers, need to add .upper()
    for filename in dir_list:
        # print('Checking', filename, 'where first symbols are', filename[:2])
        if router == filename[:2].upper() and filename.split('.')[1] == 'config':
            return lab_dir + '/' + filename
        elif router == filename[:2].upper() and filename.split('.')[1] == 'conf':
            return lab_dir + '/' + filename
        else:
            continue


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide lab number')
        sys.exit(1)
    lab_number = sys.argv[1]
    main(lab_number)


