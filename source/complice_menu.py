#!/usr/bin/python
# encoding: utf-8

### python script to interact with Complice
### initial menu
### giovanni, Saturday, April 10, 2021, 8:23 PM

from __future__ import print_function, unicode_literals

import sys
import json
import time
import datetime
from workflow import Workflow3, ICON_WEB, web
import random
import os

from config import POMOLENGTH, TIMERLENGTH, TOKEN
from complice_get import get_intentions


# get seed from environment variable or current time
seed = float(os.getenv('seed') or time.time())
# initialise RNG with seed to get deterministic values
random.seed(seed)



def main(wf):

    currTime = int (time.time())
    intentions = get_intentions()
    myIntCount = len (intentions)

    wf.rerun = 1
    wf.setvar('seed', str(seed))
    
    url= 'https://complice.co/api/v0/u/me/today/timer/all'
    params = dict(auth_token=TOKEN)
    r = web.get(url, params)


    r.raise_for_status()


    
    result = r.json()
    timerState = (result['ticker']['state'])
    
    
    if timerState == 'ticking':
        timerEnd = (result['ticker']['endTime'])
        timerEndh = datetime.datetime.fromtimestamp(int(timerEnd/1000)).strftime('%I:%M')
        timertoEnd = (timerEnd/1000) - currTime 

        timertoEndh = datetime.datetime.fromtimestamp(int(timertoEnd)).strftime('%M:%S')
        timerType = (result['ticker']['mode'])

        if timerType == 'hourglass':
            wf.rerun = 1
            wf.add_item(title="Timer running until "+timerEndh + " (↩️ to pause ⏸)",
                subtitle=timertoEndh + " left",
                icon = "icons/timer.png",
                uid="PauseRunningTimer"+ str(seed),  
                valid='TRUE',
                arg="runningTimerPause;;Timer Paused! ⌛")
            wf.add_item(title="Timer running until "+timerEndh + " (↩️ to cancel ❌)",
                subtitle=timertoEndh + " left",
                icon = "icons/timer.png",
                uid="CancelRunningTimer"+ str(seed),  
                valid='TRUE',
                arg="runningTimerCancel;;❌ Timer cancelled!")

        if timerType == 'pomo':
            wf.rerun = 1
            wf.add_item(title="Pomo running until "+timerEndh  + " (↩️ to cancel)",
                subtitle=timertoEndh + " left",
                icon = "icons/pomo.png",
                valid='TRUE',
                uid="runningPomo"+ str(seed),  
                arg="runningPomo;;❌ Pomo cancelled!")
        
    if timerState == 'breaking':
        timerEnd = (result['ticker']['endTime'])
        timerEndh = datetime.datetime.fromtimestamp(int(timerEnd/1000)).strftime('%I:%M')
        timertoEnd = (timerEnd/1000) - currTime 
        timertoEndh = datetime.datetime.fromtimestamp(int(timertoEnd)).strftime('%M:%S')
        
        wf.rerun = 1
        wf.add_item(title="enjoy your break until "+timerEndh + " (↩️ to cancel)",
            subtitle=timertoEndh + " left",
            icon = "icons/coffee.png", 
            uid="break"+ str(seed),    
            valid='TRUE',
            arg="breaking;;❌ Pomo cancelled!")   


    if timerState == 'paused':
            remTime=result['ticker']['remainingSeconds']
            wf.add_item(title="Timer paused (" + str(remTime/60) + ":" + str(remTime%60) + " left)",
                subtitle="↩️ to restart",
                icon = "icons/timerPaused.png",
                uid="pausedTimer"+ str(seed),    
                valid='TRUE',
                arg="restartTimer;;Timer Restarted!")   
            wf.add_item(title="Timer paused (" + str(remTime/60) + ":" + str(remTime%60) + " left)",
                subtitle="↩️ to cancel ❌",
                icon = "icons/timerPaused.png",
                uid="cancelTimer"+ str(seed),    
                valid='TRUE',
                arg="pausedTimerCancel;;❌ Timer cancelled!")   



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
    

        wf.add_item(title="start a " + POMOLENGTH + "-min pomo until " + pomoEnd,
            subtitle="default pomo length: " + POMOLENGTH + " min", #default length could be read from Complice, but perhaps setting in Alfred gives the user more flexibility
            icon = "icons/pomo.png",
            uid="startPomo"+ str(seed),    
            valid='TRUE',
            arg="startPomo;;Started a "+ POMOLENGTH + "-min pomo until " + pomoEnd + "! 🍅")

        wf.add_item(title="start a " + TIMERLENGTH + "-min timer until " + timerEnd,
            subtitle="default timer length: " + TIMERLENGTH + " min",
            icon = "icons/timer.png",
            uid="startTimer"+ str(seed),    
            valid='TRUE',
            arg="startTimer;;Started a "+ TIMERLENGTH + "-min timer until "+ timerEnd+"! ⏳")

        wf.add_item(title="start a "+timertoEnd30 +" timer until "+next30h,
            subtitle="top-of-the-half-hour timer",
            icon = "icons/timertarget.png",
            uid="startTimer30"+ str(seed),  
            valid='TRUE',
            arg="Timer30;;Started a "+ timertoEnd30 + " timer until " + next30h + "! 🕐")

        if next30 != next60:
            wf.add_item(title="start a "+timertoEnd60 +" timer until "+next60h,
                subtitle="top-of-the-hour timer",
                icon = "icons/timertarget.png",
                uid="startTimer60"+ str(seed),  
                valid='TRUE',
                arg="Timer60;;Started a "+ timertoEnd60 + " timer until " + next60h + "! 🕒")


     
    if myIntCount == 0:
        myMessage = "no intentions set for today"
    elif myIntCount == 1:
        myMessage= "show today's "+ str(myIntCount) + " intention"    
    else:
        myMessage= "show today's "+ str(myIntCount) + " intentions"    
    
    wf.add_item(title=myMessage,
        valid='TRUE',
        icon = "icons/complice2.png",
        uid="listIntentions"+ str(seed),
        arg="listIntentions")
    
    wf.add_item(title="post new intention",
        valid='TRUE',
        icon = "icons/addIntention.png",
        uid="newIntention"+ str(seed),
        arg="newIntention")
    

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))


