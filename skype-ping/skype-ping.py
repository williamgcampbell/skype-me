#!/usr/bin/python2.6

'''
Must be run in 32-bit mode with "arch -i386"
'''

from Skype4Py import Skype
import sys

# print usage
if len(sys.argv) < 2:
    print('usage: skype-ping.py [username] [message]')
    print('note: skype4py must be run in 32-bit architecture. Use "arch -i386" to force 32-bit mode')
    sys.exit(1)

# Retrieve system arguments
user = sys.argv[1]
message = ' '.join(sys.argv[2:])

# Create an instance of the Skype class
skype = Skype()

# Connect the Skype object to the Skype client
skype.Attach()

skype.SendMessage(user, message)