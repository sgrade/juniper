After some Ansible upgrade playbooks cannot connect to hosts.
Can be fixed with changing Ansible config (I didn't do it) or temporarily by setting env variable

export ANSIBLE_HOST_KEY_CHECKING=False

More - http://docs.ansible.com/ansible/intro_getting_started.html

