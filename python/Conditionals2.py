#!/usr/bin/python

import os

if os.getenv('USER') == "root":
  print "You are root"
elif os.getuid() == 0:
  print "You are sudo as root"
elif os.access('/etc/shadow',os.R_OK):
  print "You aren't root, but you can read shadow"
else:
  print "No soup for you"
