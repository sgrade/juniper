About
=====

Parser will replace devices' configs with the ones from some directory (e.g. provided with JNCIE bootcamp course). 
In addition, it will add base configuration, specific to your lab (SSH keys, etc.)

Note: the configs themselves are not provided here


Configuration
=============

Juniper (devices') configs
--------------------------
Configure absolute path to lab configs in "parser_configs/parser.yml"
    Note: Config files should be with ".conf" or ".config" extension (NOT archived)

Parser configs and base config
------------------------------
Configure mapping of device names to management IPs (for fxp0.0 interfaces) in "parser_configs/ip-addresses.yml"
    Note: Device names should be the same as in juniper_config_dir. For example, if config is "JS-topologies/JNCIE-SP_Bootcamp_12a_L10/configset/R1-lab6-start.config", then device name is R1
Change template for base configuration (to be merged with device config) is in "parser_configs/base.template"
    Note: IP_ADDR statement should be left as is (do NOT change it to anything else - the script will replace it with the device management IP)  


Usage
=====

python parser/parser.py lab_number

For example, if device configs for lab 10 are in
"~/JS-topologies/JNCIE-SP_Bootcamp_12a_L10"
You should run parser as 
python parser/parser.py 10

