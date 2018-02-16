from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError


def main():
    host = raw_input('Device hostname: ')
    user = raw_input('Device username: ')
    # pass = getpass("Device password: ")
    #conf = '/home/roman/JS-topologies/JNCIE-SP_Bootcamp_12a_L10/configset/R4-lab6-start.config'
    conf = raw_input('Absolute path to config file: ')
    cfg_load_pyez(host, user, conf)

def cfg_load_pyez(hostname, username, conf_file):

    try:
        dev = Device(host=hostname, user=username, password=None, gather_facts=False)
        dev.open()
    except ConnectError as err:
        print("Cannot connect to device: {0}".format(err))
        return

    dev.bind(cu=Config)

    # Lock the configuration
    print ("Locking the configuration")
    try:
        dev.cu.lock()
    except LockError as err:
        print ("Unable to lock configuration: {0}".format(err))
        dev.close()
        return

    print ("Loading configuration changes")
    try:
        dev.cu.load(path=conf_file, format='text', merge=True)
    except (ConfigLoadError, Exception) as err:
        print ("Unable to load configuration changes: {0}".format(err))
        print ("Unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError:
            print ("Unable to unlock configuration: {0}".format(err))
        dev.close()
        return

    print ("Committing the configuration")
    try:
        dev.cu.commit(comment='Loaded by example.')
    except CommitError as err:
        print ("Unable to commit configuration: {0}".format(err))
        print ("Unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError as err:
            print ("Unable to unlock configuration: {0}".format(err))
        dev.close()
        return

    # End the NETCONF session and close the connection
    dev.close()


if __name__ == "__main__":
    main()