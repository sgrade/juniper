#source code is from
#https://github.com/JNPRAutomate/ansible-junos-examples/
#modified by RomanK.net

# Two ways of getting config
# 1) With Ansible core module
cd playbook-core
ansible-playbook -i hosts pb.facts.get_config_txt.yaml
# 2) With Roles from Ansible Galaxy
cd playbook-galaxy
ansible-playbook -i hosts pb.get_facts.all.yaml
