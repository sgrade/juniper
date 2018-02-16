from __future__ import print_function
import sys
import os
from yml_parser import parse_yml


class Config:

    # Constructor
    def __init__(self, lab, device):
        """
        Put something here
        """

        # Initialize inputs
        self._lab_number = lab
        self._device = device
        self._dir_dictionary = parse_yml().get('dir')

        # We don't know the path yet - set it to None
        self._absolute_path = None
        # We haven't created path to the directory from config yet
        self._config_dir = None
        # We don't know the filename yet
        self._config_filename = None

    def _get_config_dir(self):
        if self._lab_number:
            _lab = self._lab_number
            _dir = self._dir_dictionary
            if 0 < int(self._lab_number) < 10:
                _lab = str(0) + str(_lab)
            lab_config_dir = _dir.get('top_dir') + "/" + \
                             _dir.get('subdir_level_1') + \
                             _lab + "/" + \
                             _dir.get('subdir_level_2')
            self._config_dir = lab_config_dir
            return self._config_dir
        else:
            print('Please provide lab number as CLI argument or in loader.yml')

    def _get_config_filename(self):
        # Getting list of filenames in the lab directory
        lab_dir = self._get_config_dir()
        file_list = os.listdir(lab_dir)
        # Looking for a filename, where first two letters are the same as the router name
        dev = self._device.lower()
        for filename in file_list:
            # print('Checking', filename, 'where first symbols are', filename[:2])
            if dev[:2] == filename.lower()[:2] and filename.split('.')[1] == 'config':
                # print('returning', filename)
                #return filename
                self._config_filename = filename
            elif dev[:2] == filename.lower()[:2] and filename.split('.')[1] == 'conf':
                # print('returning', filename)
                self._config_filename = filename
        return self._config_filename

    def _get_full_path(self):
        _lab_directory = self._get_config_dir()
        _config_file = self._get_config_filename()
        if _lab_directory:
            if _config_file:
                self._absolute_path = str(_lab_directory + "/" + _config_file)
        return self._absolute_path

    @property
    def path(self):
        path = self._get_full_path()
        return path


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Please provide exactly two script parameters:')
        print('1) lab number ')
        print('2) device name or IP address')
        print('for example')
        sys.exit(1)
    else:
        lab_number = sys.argv[1]
        device = sys.argv[2]
        print(Config(lab_number, device).path)