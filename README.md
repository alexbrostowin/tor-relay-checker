# tor-relay-checker
Python script that checks if a given IP is a TOR relay.

## Usage:
`tor-relay-checker.py <ip address> [<switches>]`

### IP Address:
IPv4 and IPv6 addresses are both valid. Port numbers are not valid.

### Switches (Optional):
`-h or --help`  
Displays help.

`-q or --quiet`  
Disables output. Script will still give results through return codes (see below).

## Return Codes:
### Sucessful:
#### 0
IP was found to not be in the list of active TOR nodes.
#### 1
IP was found to be in the list of active TOR nodes.

### Error:
#### 255
Help switch passed or script was run with no arguments.
#### 254
Invalid IP address was provided. IP addresses are checked using the ipaddress Python library.
#### 253
Query URL returned no response. This could be from an outage of the TOR project site or a restructuring of the site.
##### URL:
`https://onionoo.torproject.org/details?type=relay&running=true&fields=or_addresses`
