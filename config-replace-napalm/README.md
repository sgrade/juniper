About
=====

Parser will replace devices' configs with the ones from some directory (e.g. provided with JNCIE bootcamp course). 
In addition, it will add base configuration, specific to your lab (SSH keys, etc.)
 


Configuration
=============

Juniper (devices') configs
--------------------------
Lab configs are outside of the parser directory in juniper_config_dir/
Config files should be with ".conf" or ".config" extension (NOT archived)

Parser configs and base config
------------------------------
Parser configuration is in parser_configs/
ip-addresses.yml - device names and management IPs (for fxp0.0 interface)
!!! Device names should be the same as in juniper_config_dir !!!
For example, if config is "JS-topologies/JNCIE-SP_Bootcamp_12a_L10/configset/R1-lab6-start.config", then device name is R1
Base configuration (to be merged with device config) is in parser_configs/base.template



Usage
=====

python parser/parser.py lab_number

For example, if device configs for lab 10 are in
"~/JS-topologies/JNCIE-SP_Bootcamp_12a_L10"
You should run parser as 
python parser/parser.py 10
