from __future__ import print_function
from tools.yml_parser import parse_yml


class InterfaceHandler:

    def __init__(self):
        """parse loader config"""

        parsed_loader_yml = parse_yml()

    def get_used_interfaces(self):
        """parse device config and return a list of interfaces used in the lab"""
        pass

    def get_all_interfaces(self):
        """connects to a device and gets complete interface list"""
        pass

    def filter_ge_interfaces(self):
        """gets interface list and returns list of ge (Gigabit Ethernet) interfaces"""
        pass
