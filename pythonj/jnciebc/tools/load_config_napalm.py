from __future__ import print_function
import sys
import os
import napalm


def load_cfg_napalm(hostname, conf_file, username, password):
    # def config_replace(device_ip, config_file, base_config):
    """Uses NAPALM to replace device config with lab config and base config"""

    if not (os.path.exists(conf_file) and os.path.isfile(conf_file)):
        msg = 'Missing or invalid config file {0}'.format(conf_file)
        raise ValueError(msg)

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver('junos')

    # Connect:
    device = driver(hostname, username, password)
    print('Opening device ...')
    device.open()

    print('Loading lab config: ', conf_file)
    device.load_merge_candidate(filename=conf_file)

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    #print('\nDiff:')
    #print(device.compare_config())

    print('Committing ...')
    device.commit_config()

    # close the session with the device.
    device.close()
    print('Device closed.')


def main():
    """Allows using script with CLI arguments"""
    if len(sys.argv) < 4:
        print('Please provide script parameters:')
        print('1) hostname ')
        print('2) config ')
        print('3) username')
        print('4) password (mandatory for NAPALM)')
        sys.exit(1)
    else:
        hostname = sys.argv[1]
        config = sys.argv[2]
        username = sys.argv[3]
        if len(sys.argv) == 4:
            print('NAPALM library does not work without password ')
            #load_cfg_napalm(hostname, config, username, False)
        else:
            password = sys.argv[4]
            load_cfg_napalm(hostname, config, username, password)


if __name__ == '__main__':
    main()