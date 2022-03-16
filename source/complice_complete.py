#!/usr/bin/python3 
### python script to interact with Complice
### giovanni, Wednesday, April 21, 2021, 5:48 AM
## Tuesday, March 15, 2022, 3:43 PM Python3 version, no dependencies


import sys

from config import POMOLENGTH, TIMERLENGTH, TOKEN
from complice_post import complete_intention



def main():
    myInput = sys.argv[1]
    complete_intention (myInput)
    


if __name__ == "__main__":
    main()


