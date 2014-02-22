#!/bin/bash
# This script will setup the proper ip addresses for the indirect
# subnet.
# To include this script, type the following when initializing
# mininet with mn
# --pre /path/to/setup_indirect.sh
# Alternately, use init_mininet_indirect.sh to setup mininet
h1 ifconfig h1-eth0 192.168.12.1 netmask 255.255.255.0
h2 ifconfig h2-eth0 192.168.12.2 netmask 255.255.255.0
h3 ifconfig h3-eth0 192.168.12.3 netmask 255.255.255.0
h4 ifconfig h4-eth0 192.168.12.4 netmask 255.255.255.0
ids ifconfig ids-eth0 192.168.12.5 netmask 255.255.255.0
r1 ifconfig r1-eth0 192.168.12.6 netmask 255.255.255.0
h1 route add default gw 192.168.12.6
h2 route add default gw 192.168.12.6
h3 route add default gw 192.168.12.6
h4 route add default gw 192.168.12.6
r1 sysctl net.ipv4.ip_forward=1