#!/usr/bin/env python

from __future__ import print_function
import sys
from tools.yml_parser import parse_yml
from tools.get_config_path import LabConfigHandler
from tools.create_base_config import address_replace
from tools.load_config_pyez import load_cfg_pyez


class Loader:
    """Loads config to a network element"""

    def __init__(self):
        """Constructor"""

        # private attributes
        parsed_loader_yml = parse_yml()
        self._hosts = parsed_loader_yml.get('hosts')
        self._auth = parsed_loader_yml.get('auth')
        self._user = self._auth.get('user')
        self._auth_method = self._auth.get('method')
        if self._auth_method == 'password':
            self._pass = self._auth.get('password')
        else:
            self._pass = False

    def _create_base_config(self, host):
        """
        Creates base config from the template

        :param host: hostname of the device
        :type host: string
        """
        _mgmt_ip = self._hosts.get(host)
        if _mgmt_ip:
            _base_conf_filename = address_replace(_mgmt_ip)
            return _base_conf_filename
        else:
            print('Cannot get management IP from loader.yml')
            print('Ensure that hostnames in loader.yml are in lower case')
            return None

    def load_base_config(self, host):
        """
        Replaces existing network element config with the one based on template

        :param host: hostname of the device
        :type host: string
        """
        _conf = self._create_base_config(host)
        if _conf:
            _user = self._auth.get('user')
            _pass = self._auth.get('password')
            load_cfg_pyez(host, _conf, _user, _pass, mode='overwrite')
        else:
            return None

    def prepare_lab_config(self, config):
        """
        Removes unsupported lines from original config.
        E.g. Juniper's configs for JNCIE SP bootcamp are created for SRX devices.
        There is "security" section there, which is not supported by vMX - config load fails.
        NOTE: The task is solved in remove_unsupported.py -
        routine integration with other modules is to be done
        :param config:
        :return:
        """
        raise NotImplementedError

    def load_lab_config(self, lab, host):
        """
        Merges existing network element config with lab config

        :param lab: lab number
        :type lab: int
        :param host: hostname of the device
        :type host: string
        """
        _conf = LabConfigHandler(lab, host).path
        _user = self._auth.get('user')
        _pass = self._auth.get('password')
        load_cfg_pyez(host, _conf, _user, _pass, mode='merge')

    def load_all_configs(self, lab):
        """
        Load configs for all devices in the lab.

        First, it replaces current config with base configuration,
        specific to your lab (SSH keys, etc.)
        Second, it replaces devices' configs with the ones from some directory
        (e.g. provided with JNCIE bootcamp course).
        """
        for host in self._hosts:
            ip = self._hosts.get(host)
            print('')
            #print('======================')
            print('Starting with', host, 'using IP', ip)
            self.load_base_config(host)
            self.load_lab_config(lab, host)
            print('Finished with', host)
            print('======================')
        print('')
        print('Done!')
        print('')


def main():
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
        sys.exit(1)


if __name__ == '__main__':
    main()
