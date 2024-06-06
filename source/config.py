#!/usr/bin/python3 
#
#
# Sunday, April 11, 2021, 11:01 AM
#

import os
import sys

POMOLENGTH = os.path.expanduser(os.getenv('POMOLENGTH', ''))
TIMERLENGTH = os.path.expanduser(os.getenv('TIMERLENGTH', ''))
TOKEN = os.path.expanduser(os.getenv('TOKEN', ''))
USE_TIMER = os.path.expanduser(os.getenv('USE_TIMER', ''))
    

	
def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)