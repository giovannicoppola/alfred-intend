#!/usr/bin/env python
# encoding: utf-8

### python script to interact with Complice
### giovanni, Saturday, April 10, 2021, 11:20 AM


import sys
import json
import time
from datetime import datetime
from workflow import Workflow3, ICON_WEB, web
import urllib
from config import POMOLENGTH, TIMERLENGTH, TOKEN


def get_intentions():
    
    url= 'https://complice.co/api/v0/u/me/today/core.json' 
    params = dict(auth_token=TOKEN)
    r = web.get(url, params)

    r.raise_for_status()

    result = r.json()
    intentions = result['list']
   
    return intentions



def get_goals():
    
    url= 'https://complice.co/api/v0/u/me/goals/active.json' 
    params = dict(auth_token=TOKEN)
    r = web.get(url, params)

    r.raise_for_status()

    result = r.json()
    goals = result['goals']
    
    
    return goals




def main(wf):
    
    intentions = get_intentions()
    
    
           
    for myIntention in intentions:
        if 'd' in myIntention:
             subString="✅ Completed"
             myArg = ""
        else:
            subString="↩️ to complete"
            myArg = myIntention['zid']

        wf.add_item(title=myIntention['text'],
            subtitle=subString,
            valid='TRUE',
            arg=myArg)
      
    wf.send_feedback()




if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))


