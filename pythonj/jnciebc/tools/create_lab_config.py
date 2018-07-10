from __future__ import print_function
import shutil

from get_config_path import lab_config_handler


def remove_unsupported(conf):

    # vMX does not support the following
    unsupported_statement = """security {
        forwarding-options {
            family {
                inet6 {
                    mode packet-based;
                }
                mpls {
                    mode packet-based;
                }
                iso {
                    mode packet-based;
                }
            }
        }
    }"""

    with open(conf, 'r+') as c:
        c_lines = c.readlines()
        c_lines_stripped = [line.strip() for line in c_lines]

        start_index = c_lines_stripped.index("security {")
        section_length = len(unsupported_statement.split('\n'))
        end_index = start_index + section_length

        updated_content = ("".join(c_lines[:start_index] + c_lines[end_index:]))

        c.seek(0)
        c.truncate(0)
        c.write(updated_content)


def prepare_lab_config(lab, host):
    """
    Creates base device config from base template.

    Replaces the IP_ADDR in the template with the device's IP address
    :param ip_address: device management IP address
    :return: base config file name
    """

    _conf = lab_config_handler(lab, host).path

    # copy the config to temp directory
    print('Preparing lab config for', host)
    tmp_file = '/tmp/lab.' + str(host)
    shutil.copyfile(_conf, tmp_file)

    # further operations will be with the tmp config to avoid breaking original config
    # remove unsupported lines
    try:
        remove_unsupported(tmp_file)
        print('Lab config returned:', tmp_file)
        return tmp_file
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # create_lab_config(lab_number, hostname)
    lab_number = 8
    hostname = 'vrdevice'
    prepare_lab_config(lab_number, hostname)
