# encoding: utf-8
### python script to interact with Complice
### giovanni, Saturday, April 10, 2021, 2:11 PM

from __future__ import print_function, unicode_literals

import sys
from workflow import Workflow3, ICON_WEB, web
import time
import re
import json


from config import POMOLENGTH, TIMERLENGTH, TOKEN


def complete_intention(myID):
    
    
    url = 'https://complice.co/api/v0/u/me/completeById/'+myID
    
       
    datastring = dict()
    datastring['auth_token'] = TOKEN
    
    r = web.post(url, params=datastring)
  
    r.raise_for_status()


def start_custom_hourglass30():
    url = 'https://complice.co/api/v0/u/me/today/timer/hourglass'

# calculating endTIme in milliseconds to the next half hour
    
    currTime = int (time.time())
    
    
    next30 = (currTime - (currTime % 1800)) + 1800
    end_millis = int((next30 * 1000)+100)
    
    

    datastring = dict()
    datastring['auth_token'] = TOKEN
    datastring['mode'] = "hourglass"
    datastring['state'] = "ticking"
    datastring['endTime'] = end_millis
    
    r = web.post(url, params=datastring)
    
# debug
   # with open("myOut.txt", 'a') as f:
    #    f.write ('\n'+str(currTime)+' - ')
     #   f.write (url +' - ')
      #  f.write(json.dumps(datastring))
    




def start_custom_hourglass60():
    url = 'https://complice.co/api/v0/u/me/today/timer/hourglass'

# calculating endTIme in milliseconds to the next half hour
    
    currTime = int (time.time())
    
    
    
    next60 = (currTime - (currTime % 3600)) + 3600
    end_millis = int((next60 * 1000)+100)
    
    
    datastring = dict()
    datastring['auth_token'] = TOKEN
    datastring['mode'] = "hourglass"
    datastring['state'] = "ticking"
    datastring['endTime'] = end_millis
    
    r = web.post(url, params=datastring)

    # debug
    #with open("myOut.txt", 'a') as f:
    #    f.write ('\n'+str(currTime)+' - ')
    #    f.write (url +' - ')
    #    f.write(json.dumps(datastring))
    



def post_intention(myTextInput):
    

    url = 'https://complice.co/api/v0/u/me/intentions?auth_token='+TOKEN
       
    
    datastring = dict()
    
    datastring['raw'] = myTextInput
    headers = {'Content-Type: application/json'}
    r = web.post(url, data=datastring,headers=headers)
    r.raise_for_status()



def start_pomo():
    
    
    url = 'https://complice.co/api/v0/u/me/today/timer/startpomodoro'
    
    
    datastring = dict()
    datastring['auth_token'] = TOKEN
    datastring['duration'] = POMOLENGTH
    r = web.post(url, params=datastring)
    
    r.raise_for_status()
    


def cancel_timer():
    
    
    url = 'https://complice.co/api/v0/u/me/today/timer/cancel'
    
    
    datastring = dict()
    datastring['auth_token'] = TOKEN
    
    r = web.post(url, params=datastring)
    r.raise_for_status()




def pause_timer():
    
    
    url = 'https://complice.co/api/v0/u/me/today/timer/pause'
    
    
    datastring = dict()
    datastring['auth_token'] = TOKEN
    
    r = web.post(url, params=datastring)
    r.raise_for_status()


def start_hourglass():
   
    
    url = 'https://complice.co/api/v0/u/me/today/timer/hourglass'
    #currTime = int (time.time()) #this is for debugging
     
    datastring = dict()
    datastring['auth_token'] = TOKEN
    datastring['duration'] = TIMERLENGTH
    r = web.post(url, params=datastring)
    
    r.raise_for_status()
    # debugging
    #with open("myOut.txt", 'a') as f:
    #    f.write ('\n'+str(currTime)+' - ')
    #    f.write (url +' - ')
    #    f.write(json.dumps(datastring))



def restart_hourglass():
   
    
    url = 'https://complice.co/api/v0/u/me/today/timer/unpause'
    
    
    datastring = dict()
    datastring['auth_token'] = TOKEN
    r = web.post(url, params=datastring)
    

    r.raise_for_status()
  
 



def main(wf):
    myInput = wf.args[0]
    post_intention (myInput)
    
    


if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))

