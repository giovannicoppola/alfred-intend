#!/usr/bin/python3 

### python script to interact with Complice
### giovanni, Saturday, April 10, 2021, 2:11 PM
## Tuesday, March 15, 2022, 3:43 PM Python3 version, no dependencies


import sys
import time
from config import POMOLENGTH, TIMERLENGTH, TOKEN
from lib import requests
from lib.requests.structures import CaseInsensitiveDict

import os


def startMenubar(menubarLength):

    
    from subprocess import Popen, PIPE, run


    sprintDurSec = str(int(menubarLength) * 60)
    scpt = '''
        on run {sprintDur, Email_Start, Email_StartF, sprintDurSec}
            display notification ("Starting " & menubarLength & "-min pomo 💪.. GO!") with title (Email_StartF & " emails to clear") subtitle (sprintDur & " min sprint") sound name "Frog"

                
            tell application "Menubar Countdown"
        
                set hours to 0
                set minutes to sprintDur
                set seconds to 0
                set play alert sound to false
                set repeat alert sound to false
                set show alert window to false
                set show notification to false
                set play notification sound to false
                set speak announcement to false
                start timer
        
            
            delay (sprintDurSec as integer)
            
                stop timer
                end tell

            
            
            display dialog (menubarLength & "-min pomo completed ✅") with title "Intend pomo completed" buttons {"OK"} default button "OK" giving up after 10 with icon POSIX file ("icon.png" as string)
            
        end run'''

    args = [menubarLength]
            
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
        




def complete_intention(myID):
    
    url = "https://complice.co/api/v0/u/me/completeById/"+myID+"?auth_token="+TOKEN # not sure why I can't pass TOKEN with the JSON string
    headers = CaseInsensitiveDict()
    headers["Content-Length"] = "0"
    resp = requests.post(url, headers=headers)
    #print(resp.status_code)





def start_custom_hourglass60():
    url = 'https://complice.co/api/v0/u/me/today/timer/hourglass?auth_token='+TOKEN  

# calculating endTIme in milliseconds to the next half hour
    
    currTime = int (time.time())
    next60 = (currTime - (currTime % 3600)) + 3600
    end_millis = int((next60 * 1000)+100)
       
    datastring = dict()
    
    datastring['mode'] = "hourglass"
    datastring['state'] = "ticking"
    datastring['endTime'] = end_millis
    
    requests.post(url, data=datastring)


def start_custom_hourglass30():
    url = 'https://complice.co/api/v0/u/me/today/timer/hourglass?auth_token='+TOKEN  

# calculating endTIme in milliseconds to the next half hour
    
    currTime = int (time.time())
    next30 = (currTime - (currTime % 1800)) + 1800
    end_millis = int((next30 * 1000)+100)
    
    

    datastring = dict()
    datastring['mode'] = "hourglass"
    datastring['state'] = "ticking"
    datastring['endTime'] = end_millis
    
    requests.post(url, data=datastring)
    
# debug
   # with open("myOut.txt", 'a') as f:
    #    f.write ('\n'+str(currTime)+' - ')
     #   f.write (url +' - ')
      #  f.write(json.dumps(datastring))
    



def post_intention(myTextInput):
    

    url = 'https://complice.co/api/v0/u/me/intentions?auth_token='+TOKEN
    datastring = dict()
    
    datastring['raw'] = myTextInput
    requests.post(url,data=datastring)
    


def start_pomo():
    
    url = "https://complice.co/api/v0/u/me/today/timer/startpomodoro?auth_token="+TOKEN  
    datastring = CaseInsensitiveDict()
    datastring['duration'] = POMOLENGTH
    resp = requests.post(url, data=datastring)
    print(resp.status_code)
    startMenubar (POMOLENGTH)
    


def cancel_timer():
    url = 'https://complice.co/api/v0/u/me/today/timer/cancel?auth_token='+TOKEN
    requests.post(url)

def pause_timer():
    
    url = 'https://complice.co/api/v0/u/me/today/timer/pause?auth_token='+TOKEN  
    requests.post(url)
    
    

def start_hourglass():
    url = "https://complice.co/api/v0/u/me/today/timer/hourglass?auth_token="+TOKEN  
    datastring = CaseInsensitiveDict()
    
    datastring['duration'] = TIMERLENGTH
    requests.post(url, params=datastring)
        
    # debugging
    #with open("myOut.txt", 'a') as f:
    #    f.write ('\n'+str(currTime)+' - ')
    #    f.write (url +' - ')
    #    f.write(json.dumps(datastring))



def restart_hourglass():
    url = 'https://complice.co/api/v0/u/me/today/timer/unpause?auth_token='+TOKEN  
    requests.post(url)
    

def main():
    myInput = sys.argv[1]
    post_intention (myInput)
    

if __name__ == "__main__":
    main()