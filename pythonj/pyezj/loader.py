from __future__ import print_function
from tools.yml_parser import parse_yml
from tools.device_config_path import Config


#hostname = input("Device hostname: ")
#host = '172.16.30.204'
#username = input("Device username: ")
#user = 'roman'
#password = getpass("Device password: ")

#conf = '/home/roman/JS-topologies/JNCIE-SP_Bootcamp_12a_L10/configset/R4-lab6-start.config'


class Loader:


    # Constructor
    def __init__(self):
        """
        kvargs['notify']
          event notify callback
        """

        #
        # private attributes
        #
        parsed_loader_yml = parse_yml()
        self._dir = parsed_loader_yml.get('dir')
        self._auth = parsed_loader_yml.get('auth')
        self._hosts = parsed_loader_yml.get('hosts')




x = Loader()
#x.work_dir()

print(Config(7, 'vrdevice').path)
