from __future__ import print_function


def remove_unsupported(filename, section):
    with open(filename, 'r+') as f:
        content = f.read().replace(section, '')
        print(content)


filename = '/home/roman/JS-topologies/JNCIE-SP_Bootcamp_12a_L10/configset/VR-lab6-start.config'
section = """security {
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
}
"""


remove_unsupported(filename, section)
