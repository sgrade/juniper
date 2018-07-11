#!/usr/bin/env python3

import os
import subprocess

def save_conf(vars_filename):
    with open(vars_filename, 'r') as a_file:
        lines = a_file.readlines()

        for line in lines:
            line_splitted = line.strip("\n").split(": ")

            if line_splitted[0] == 'course_name':
                course_name = line_splitted[1]

            if line_splitted[0] == 'section_name':
                section_name = line_splitted[1]

    a_file.close()

    full_path = 'configs/'+course_name+'/'+section_name

    try:
        os.makedirs(full_path)
    except OSError:
        if not os.path.isdir(full_path):
            raise

    result = subprocess.run(["ansible-playbook", "-i", "playbook-core/hosts", "playbook-core/pb.junos_facts.prepare_one_config-txt.yml"])
    print(result)

if __name__ == '__main__':
    save_conf('external_vars.yml')
