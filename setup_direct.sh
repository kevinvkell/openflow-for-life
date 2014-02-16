#!/bin/bash
# This script will setup the proper ip addresses for the direct
# subnet. It is not required for the indirect subnet
# To include this script, type the following when initializing
# mininet with mn
# --pre /path/to/setup_direct.sh
h1 ifconfig h1-eth0 192.168.12.1 netmask 255.255.255.0
h2 ifconfig h2-eth0 192.168.12.2 netmask 255.255.255.0
h3 ifconfig h3-eth0 192.168.12.3 netmask 255.255.255.0
h4 ifconfig h4-eth0 192.168.12.4 netmask 255.255.255.0
r1 ifconfig r1-eth0 192.168.23.6 netmask 255.255.255.0
ids ifconfig ids-eth0 192.168.12.5 netmask 255.255.255.0
ids ifconfig ids-eth1 192.168.23.5 netmask 255.255.255.0
h1 route add default gw 192.168.12.5
h2 route add default gw 192.168.12.5
h3 route add default gw 192.168.12.5
h4 route add default gw 192.168.12.5
r1 route add default gw 192.168.23.5
ids sysctl net.ipv4.ip_forward=1
h1 arp -s 192.168.12.2 00:00:00:00:00:05
h1 arp -s 192.168.12.3 00:00:00:00:00:05
h1 arp -s 192.168.12.4 00:00:00:00:00:05
h2 arp -s 192.168.12.1 00:00:00:00:00:05
h2 arp -s 192.168.12.3 00:00:00:00:00:05
h2 arp -s 192.168.12.4 00:00:00:00:00:05
h3 arp -s 192.168.12.1 00:00:00:00:00:05
h3 arp -s 192.168.12.2 00:00:00:00:00:05
h3 arp -s 192.168.12.4 00:00:00:00:00:05
h4 arp -s 192.168.12.1 00:00:00:00:00:05
h4 arp -s 192.168.12.2 00:00:00:00:00:05
h4 arp -s 192.168.12.3 00:00:00:00:00:05
