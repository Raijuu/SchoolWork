#!/usr/bin/python2.7

import sys

#get adddress string and cidr string from cli
(addrString,cidrString) = sys.argv[1].split('/')

#split address into octets and change cidr to an int
addr = addrString.split('.')
cidr = int(cidrString)

#initialize mask and calculate based on cidr mask value given.
mask = [0,0,0,0]
for i in range(cidr):
  mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

#initialize net and binary and netmask with addr to get the network
net = []
for i in range(4):
  net.append(int(addr[i]) & mask[i])

# Determine broadcast parameters from CIDR address and duplicate the
# network address
broad = list(net)
brange = 32 - cidr
for i in range(brange):
  broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

#print info, map int list to strings for great justice.
print "Address: " , addrString
print "Netmask: " , ".".join(map(str,mask))
print "Network: " , ".".join(map(str,net))
print "Broadcast: " , ".".join(map(str,broad))

