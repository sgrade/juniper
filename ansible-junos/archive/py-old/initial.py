#!/usr/bin/env python3

import os
import subprocess

def initial_conf():

    result = subprocess.run(["ansible-playbook", "-i", "playbook-core/hosts", "playbook-core/pb.junos_config.initial-text.yml"])
    print(result)

if __name__ == '__main__':
    initial_conf()
