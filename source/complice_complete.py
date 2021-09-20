# encoding: utf-8
### python script to interact with Complice
### giovanni, Wednesday, April 21, 2021, 5:48 AM


import sys
from workflow import Workflow3, ICON_WEB, web
import time
import re

import requests
import json


from config import POMOLENGTH, TIMERLENGTH, TOKEN


def complete_intention(myID):
    
    
    url = 'https://complice.co/api/v0/u/me/completeById/'+myID
    
       
    datastring = dict()
    datastring['auth_token'] = TOKEN
    
    r = web.post(url, params=datastring)
    r.raise_for_status()





def main(wf):
    myInput = wf.args[0]
    complete_intention (myInput)
    
    


if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))

