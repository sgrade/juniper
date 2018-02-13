from __future__ import print_function

import napalm
import sys
import os


def config_replace(device_ip, config_file, base_config):
    """
    Uses NAPALM to replace device config with lab config and base config
    :param device_ip: management IP (fxp0.0)
    :param config_file: lab config (e.g. provided with JNCIE bootcamp course)
    :param base_config: specific parameters to complement the lab config
    :return: None
    """


    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = 'Missing or invalid config file {0}'.format(config_file)
        raise ValueError(msg)

    print('Loading config file', config_file.split('JS-topologies/')[1])

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver('junos')

    # Connect:
    device = driver(hostname=device_ip, username='roman',
                    password='junos1')

    print('Opening device ...')
    device.open()

    print('Loading lab config ...')
    device.load_replace_candidate(filename=config_file)

    print('Loading base config ...')
    device.load_merge_candidate(filename=base_config)

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    print('\nDiff:')
    print(device.compare_config())

    # You can commit or discard the candidate changes.
    try:
        choice = raw_input("\nCommit? [yN]: ")
    except NameError:
        choice = input("\nCommit? [yN]: ")
    if choice == 'y' or choice == 'Y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()

    # close the session with the device.
    device.close()
    print('Device closed.')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Please supply device name, lab config, base config')
        sys.exit(1)
    dev_ip = sys.argv[1]
    lab_conf = sys.argv[2]
    base_conf = sys.argv[3]
    config_replace(dev_ip, lab_conf, base_conf)

