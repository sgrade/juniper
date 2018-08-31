from pprint import pprint
from jnpr.junos import Device

dev = Device(host='172.16.29.201', user='roman', password='junos1' )
dev.open()

pprint( dev.facts )

dev.close()
