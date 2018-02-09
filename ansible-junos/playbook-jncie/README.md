Usage
=====

Provide lab number as extra argument.
If lab number is < 10, prepend with leading zero

For example, for lab No. 9
ansible-playbook -i hosts pb.override_configs.yaml -e "lab=09"
