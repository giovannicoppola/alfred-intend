#!/usr/bin/python3


### python script to interact with Complice
### initial menu
### giovanni, Saturday, April 10, 2021, 8:23 PM
## updated to Python3, February 2022


import time
import datetime
import random
import os

from config import POMOLENGTH, TIMERLENGTH, TOKEN
from complice_get import get_intentions
import urllib.request 
import json

from urllib.parse import urlencode
import sys


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

# get seed from environment variable or current time
seed = float(os.getenv('seed') or time.time())
# initialise RNG with seed to get deterministic values
random.seed(seed)






currTime = int (time.time())
intentions = get_intentions()
#log (intentions)
myIntCount = len (intentions)

result = {"rerun": 1,
"variables": {
        "seed": str(seed)
    },
    "items": []}

url= 'https://intend.do/api/v0/u/me/today/timer/all'
params = urlencode({'auth_token':TOKEN}) 
myURL=url+"?"+params
URLrequest = urllib.request.Request(myURL)

with urllib.request.urlopen(URLrequest) as URLresponse: 
        resultURL = json.load(URLresponse)
        

timerState = (resultURL['ticker']['state'])


if timerState == 'ticking':
    timerEnd = (resultURL['ticker']['endTime'])
    timerEndh = datetime.datetime.fromtimestamp(int(timerEnd/1000)).strftime('%I:%M')
    timertoEnd = (timerEnd/1000) - currTime 

    timertoEndh = datetime.datetime.fromtimestamp(int(timertoEnd)).strftime('%M:%S')
    timerType = (resultURL['ticker']['mode'])

    if timerType == 'hourglass':
        #wf.rerun = 1
        result["items"].append({
            "title": "Timer running until "+timerEndh + " (↩️ to pause ⏸)",
            "subtitle": timertoEndh + " left",
            
            "icon": {
                                        "path": "icons/timer.png"
                                    },
            "valid":'TRUE',
            "uid":"PauseRunningTimer"+ str(seed), 
            
            "arg":"runningTimerPause;;Timer Paused! ⌛"           })
                
        
        result["items"].append({
            "title": "Timer running until "+timerEndh + " (↩️ to cancel ❌)",
            "subtitle": timertoEndh + " left",
            
            "icon": {
                                        "path": "icons/timer.png"
                                    },
            "valid":'TRUE',
            "uid":"CancelRunningTimer"+ str(seed),  
            
            "arg":"runningTimerCancel;;❌ Timer cancelled!"})
            
        

    if timerType == 'pomo':
        #wf.rerun = 1
        result["items"].append({
            "title": "Pomo running until "+timerEndh  + " (↩️ to cancel)",
            "subtitle": timertoEndh + " left",
            
            "icon": {
                                        "path": "icons/pomo.png"
                                    },
            "valid":'TRUE',
            "uid":"runningPomo"+ str(seed),  
            
            "arg":"runningPomo;;❌ Pomo cancelled!"})
        
            
                
if timerState == 'breaking':
    timerEnd = (resultURL['ticker']['endTime'])
    timerEndh = datetime.datetime.fromtimestamp(int(timerEnd/1000)).strftime('%I:%M')
    timertoEnd = (timerEnd/1000) - currTime 
    timertoEndh = datetime.datetime.fromtimestamp(int(timertoEnd)).strftime('%M:%S')
    
    #wf.rerun = 1
    result["items"].append({
            "title": "enjoy your break until "+timerEndh + " (↩️ to cancel)",
            "subtitle": timertoEndh + " left",
            
            "icon": {
                                        "path": "icons/coffee.png"
                                    },
            "valid":'TRUE',
            "uid":"break"+ str(seed),    
            
            "arg":"breaking;;❌ Pomo cancelled!"  })
        
        
if timerState == 'paused':
        remTime=resultURL['ticker']['remainingSeconds']
        result["items"].append({
            "title": "Timer paused (" + str(int(remTime/60)) + ":" + str(remTime%60) + " left)",
            "subtitle": "↩️ to restart",
            
            "icon": {
                                        "path": "icons/timerPaused.png"
                                    },
            "valid":'TRUE',
            "uid":"pausedTimer"+ str(seed),
            
            "arg":"restartTimer;;Timer Restarted!"   })
        
        result["items"].append({
            "title": "Timer paused (" + str(int(remTime/60)) + ":" + str(remTime%60) + " left)",
            "subtitle": "↩️ to cancel ❌",
            
            "icon": {
                                        "path": "icons/timerPaused.png"
                                    },
            "valid":'TRUE',
            "uid": "cancelTimer"+ str(seed),    
            
            "arg":"pausedTimerCancel;;❌ Timer cancelled!"           })
        

            


if timerState == 'inactive':

    next30 = (currTime - (currTime % 1800)) + 1800
    next60 = (currTime - (currTime % 3600)) + 3600

    next30h = datetime.datetime.fromtimestamp(int(next30)).strftime('%I:%M')
    next60h = datetime.datetime.fromtimestamp(int(next60)).strftime('%I:%M')

    timertoEnd30 = (next30) - currTime
    timertoEnd30 = datetime.datetime.fromtimestamp(int(timertoEnd30)).strftime('%M:%S')

    timertoEnd60 = (next60) - currTime
    timertoEnd60 = datetime.datetime.fromtimestamp(int(timertoEnd60)).strftime('%M:%S')

    pomoEnd = currTime + (int(POMOLENGTH)*60)
    pomoEnd = datetime.datetime.fromtimestamp(int(pomoEnd)).strftime('%I:%M')

    timerEnd = currTime + (int(TIMERLENGTH)*60)
    timerEnd = datetime.datetime.fromtimestamp(int(timerEnd)).strftime('%I:%M')
    
    result["items"].append({
        "title": "start a " + POMOLENGTH + "-min pomo until " + pomoEnd,
        "subtitle": "default pomo length: " + POMOLENGTH + " min", 
            #default length could be read from Complice, but perhaps setting in Alfred gives the user more flexibility
            "icon": {
                                        "path": "icons/pomo.png"
                                    },
            "valid":'TRUE',
            "uid":"startPomo"+ str(seed),    
            
            "arg":"startPomo;;Started a "+ POMOLENGTH + "-min pomo until " + pomoEnd + "! 🍅"})
        

    result["items"].append({
            "title": "start a " + TIMERLENGTH + "-min timer until " + timerEnd,
            "subtitle": "default timer length: " + TIMERLENGTH + " min",
            
            "icon": {
                                        "path": "icons/timer.png"
                                    },
            "valid":'TRUE',
            "uid":"startTimer"+ str(seed),    
            
            "arg":"startTimer;;Started a "+ TIMERLENGTH + "-min timer until "+ timerEnd+"! ⏳"           })
        

    result["items"].append({
            "title": "start a "+timertoEnd30 +" timer until "+next30h,
            "subtitle": "top-of-the-half-hour timer",
            
            "icon": {
                                        "path": "icons/timertarget.png"
                                    },
            "valid":'TRUE',
            "uid":"startTimer30"+ str(seed),  
            
            "arg":"Timer30;;Started a "+ timertoEnd30 + " timer until " + next30h + "! 🕐"})
        
    
    if next30 != next60:
        result["items"].append({
            "title": "start a "+timertoEnd60 +" timer until "+next60h,
            "subtitle": "top-of-the-hour timer",
            
            "icon": {
                                        "path": "icons/timertarget.png"
                                    },
            "valid":'TRUE',
            "uid":"startTimer60"+ str(seed),  
            
            "arg":"Timer60;;Started a "+ timertoEnd60 + " timer until " + next60h + "! 🕒"})
        
        
    
if myIntCount == 0:
    myMessage = "no intentions set for today"
elif myIntCount == 1:
    myMessage= "show today's "+ str(myIntCount) + " intention"    
else:
    myMessage= "show today's "+ str(myIntCount) + " intentions"    


result["items"].append({
        "title": myMessage,

        
        "icon": {
                                    "path": "icons/complice2.png"
                                },
        "valid":'TRUE',
        "uid":"listIntentions"+ str(seed), 
        
        "arg":"listIntentions"           })
    

result["items"].append({
        "title": "post new intention",

        
        "icon": {
                                    "path": "icons/addIntention.png"
                                },
        "valid":'TRUE',
        "uid":"newIntention"+ str(seed), 
        
        "arg":"newIntention"           })
    



# Send the results to Alfred as JSON
print (json.dumps(result))





