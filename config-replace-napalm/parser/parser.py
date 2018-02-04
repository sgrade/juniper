from __future__ import print_function

import os
import sys
import yaml
from config_replace import config_replace
from ip_replace import address_replace


work_dir = os.getcwd()


def parser(lab_num):

    address_config = parse_ip_addresses(work_dir+'/parser_configs/ip-addresses.yml')

    for router, ip in address_config.items():
        print('')
        print('======================')
        print('Starting with', router, 'using IP', ip)
        lab_config = find_config(lab_num, router)
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
        addr_cfg = yaml.load(ymlfile)
        return addr_cfg


def find_config(lab, router):
    """
    Looking for the router's config in the lab directory
    :rtype: string
    """

    # Lab number should be with a leading zero
    global lab_dir
    if int(lab) < 10:
        lab = str(0) + str(lab)

    parser_config = work_dir + '/parser_configs/parser.yml'
    with open(parser_config) as ymlfile:
        parser_cfg = yaml.load(ymlfile)
        for key, value in parser_cfg.items():
            if key == 'lab_config_dir':
                lab_cfg_dir = value
            elif key == 'subdirectory_prefix':
                subdir_prefix = value
            elif key == 'configdir_in_subdirectory':
                confdir_in_subdir = value

        lab_dir = lab_cfg_dir + '/' + subdir_prefix + lab + '/' + confdir_in_subdir

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
    parser(lab_number)


