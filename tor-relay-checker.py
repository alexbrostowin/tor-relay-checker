#!/usr/bin/env python3

import sys
from urllib.request import urlopen
import json
from ipaddress import ip_address, IPv4Address

def validateIP(IP: str) -> int:
    try:
        return 0 if type(ip_address(IP)) is IPv4Address else 1
    except ValueError:
        return -1

def help():
    file = open("help.txt", "r")
    print(file.read())
    file.close()

if __name__ == "__main__":
    #SWITCHES
    if len(sys.argv) < 2 or ("-h" or "--help") in sys.argv:
        help()
        sys.exit(255)
    
    quiet: bool = False
    if ("-q" or "--quiet") in sys.argv:
        quiet = True
    
    #IP Checking 
    IPAddress: str = sys.argv[1]
    IPType: int = validateIP(IPAddress)
    
    if IPType == -1:
        if not quiet:
            print("ERR:", IPAddress, "is not a valid IP.")
        sys.exit(254)

    #Load JSON from URL
    url: str = "https://onionoo.torproject.org/details?type=relay&running=true&fields=or_addresses"
    try:
        response = urlopen(url)
    except:
        if not quiet:
            print ("ERR:", url, "returned no response.")
        sys.exit(253)

    data = json.loads(response.read())
    response.close()

    #Iterate JSON
    code: int = 0
    for i in data['relays']:
        try:
            if IPAddress in i['or_addresses'][IPType]:
                code = 1
                break
        except:
            continue

    #Return result
    if not quiet:
        if code == 0:
            print (IPAddress, "is not an active TOR relay.")
        elif code == 1:
            print (IPAddress, "is an active TOR relay.")
    sys.exit(code)
