Configs for Juniper vMX routers for the following lab:
"JNCIE Service Provider Bootcamp (JNCIE-SP-12.a)"

Note: 
These are NOT official configs from Juniper Networks. 
I (www.RomanK.net) created the configs myself using lab diagrams and lab guides.
The majority of the bootcamp labs work, but some things don't. E.g.: 
- LACP on aggregated Ethernet interfaces are not supported by vMXs (at least up to JunOS 17.4) - disable LACP manually
- BFD syntax changed in recent versions of JunOS
- physical topology of the labs have minor differences - there might be minor changes required in the links between vMXs
