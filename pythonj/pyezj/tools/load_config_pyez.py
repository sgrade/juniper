from __future__ import print_function
import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError


def cfg_load_pyez(hostname, username, conf_file, mode='overwrite'):

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

    print("Loading config: ", conf_file)
    if mode.lower() == 'overwrite':
        try:
            #dev.cu.load(path=conf_file, format='text', merge=True)
            dev.cu.load(path=conf_file, format='text', overwrite=True)
        except (ConfigLoadError, Exception) as err:
            print ("Unable to load configuration changes: {0}".format(err))
            print ("Unlocking the configuration")
            try:
                dev.cu.unlock()
            except UnlockError:
                print ("Unable to unlock configuration: {0}".format(err))
            dev.close()
            return
    elif mode.lower() == 'merge':
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


def main():
    """Allows using script with CLI arguments"""
    if len(sys.argv) != 4:
        print('Please provide exactly three script parameters:')
        print('1) hostname ')
        print('2) username ')
        print('3) config')
        sys.exit(1)
    else:
        hostname = sys.argv[1]
        username = sys.argv[2]
        config = sys.argv[3]
        cfg_load_pyez(hostname, username, config)


if __name__ == '__main__':
    main()