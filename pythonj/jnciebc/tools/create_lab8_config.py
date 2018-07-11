from __future__ import print_function
import sys
from get_config_path import lab_config_handler
from create_lab_config import remove_unsupported


def prepare_one_config(dir, conf):

    config_path = str(dir+'/'+conf)
    print('processing config: ', config_path)

    with open(config_path, 'r') as c:
        # get the config except first two lines like these ones
        #   "## Last changed: 2011-07-27 18:02:14 UTC"
        #   "version 10.3D0;"
        c_lines = c.readlines()[2:]

        # remove "system" section
        line_index = 0
        for line in c_lines:
            if line.startswith("}"):
                line_index = c_lines.index(line)
                print(line, line_index)
                break
        del(c_lines[:line_index+1])

        # remove interface descriptions as they lead to "syntax error" when committing under logical systems
        for line in c_lines:
            if line.lstrip().startswith("description"):
                c_lines.remove(line)

        return "".join(c_lines)


def create_custom_config(lab, host, configs):
    """
    Creates base device config from base template.

    Replaces the IP_ADDR in the template with the device's IP address
    :param ip_address: device management IP address
    :return: base config file name
    """

    _conf_dir = lab_config_handler(lab, host).lab_dir

    print('Preparing custom config')
    tmp_file = '/tmp/custom.' + lab + str(host)
    with open(tmp_file, 'w') as f:
        f.write('logical-systems {\n')

        # create separate logical system for each config and the configs there
        for config in configs:

            # create logical system
            logical_system_name = config.split(".")[0].lower()
            f.write(str(logical_system_name + " {\n"))

            # write config
            f.write(prepare_one_config(_conf_dir, config))

            # closing respective logical system
            f.write('}\n')

        # closing logical-systemS
        f.write('}\n')

    return tmp_file


if __name__ == "__main__":
    # create_lab_config(lab_number, hostname)
    if len(sys.argv) > 3:
        _lab_number = sys.argv[1]
        _host = sys.argv[2]
        create_custom_config(_lab_number, _host, sys.argv[3:])
    else:
        print('Please provide CLI arguments: ')
        print('lab number, hostname/IP, config1, config2, ..., configN')
        print('allowed lab numbers: 1, 2, ... 11')
        print('allowed host names: r1, r2, r3, r4, r5, vrdevice')
