#source code is from
#https://github.com/JNPRAutomate/ansible-junos-examples/
#modified by RomanK.net

# Two ways of getting config
# 1) With Ansible core module
ansible-playbook -i hosts playbook-core/pb.facts.get_config_txt.yaml
# 2) With Roles from Ansible Galaxy
ansible-playbook -i hosts playbook-galaxy/pb.get_facts.all.yaml
