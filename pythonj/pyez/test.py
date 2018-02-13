from jnpr.junos import Device
from getpass import getpass
import sys

#hostname = input("Device hostname: ")
hostname = '172.16.30.209'
#username = input("Device username: ")
username = 'roman'
#password = getpass("Device password: ")
password = 'junos1'

# NETCONF session over SSH
dev = Device(host=hostname, user=username, passwd=password)

# Telnet connection
#dev = Device(host=hostname, user=username, passwd=password, mode='telnet', port='23')

# Serial console connection
#dev = Device(host=hostname, user=username, passwd=password, mode='serial', port='/dev/ttyUSB0')

try:
    dev.open()
except Exception as err:
    print (err)
    sys.exit(1)

print (dev.facts)
dev.close()
