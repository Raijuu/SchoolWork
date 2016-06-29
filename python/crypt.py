#!/usr/bin/python2.7

import sys
import crypt
f = open(sys.argv[1],"r")
lines = f.readlines()
f.close()

for line in lines:
  data = line.split(':')
  #Set username and password from first two fields.
  user,password = data[0:2]
  geco = data[4].split(',')

  #Create password guess using first char of first name and last field
  guess = geco[0][0] + geco[-1]

  #assign salt as first two characters of crypted password
  salt = password[0:2]

if crypt.crypt(guess.salt)
