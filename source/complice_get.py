#!/usr/bin/python3 

### python script to interact with Complice
### giovanni, Saturday, April 10, 2021, 11:20 AM
## version 0.2 for Python3


import json
from datetime import datetime
import urllib
from config import POMOLENGTH, TIMERLENGTH, TOKEN
import urllib.request 
from urllib.parse import urlencode


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

def get_intentions():
    
    url= 'https://complice.co/api/v0/u/me/today/core.json' 
    params = urlencode({'auth_token':TOKEN}) 
    myURL=url+"?"+params
   
    URLrequest = urllib.request.Request(myURL)

    with urllib.request.urlopen(URLrequest) as URLresponse: 
            resultURL = json.load(URLresponse)
            intentions = resultURL['list']
   
    return intentions



def get_goals():
    
    url= 'https://complice.co/api/v0/u/me/goals/active.json' 
    params = urlencode({'auth_token':TOKEN}) 
    myURL=url+"?"+params
   
    URLrequest = urllib.request.Request(myURL)

    with urllib.request.urlopen(URLrequest) as URLresponse: 
            resultURL = json.load(URLresponse)
            goals = resultURL['goals']
    
    
    return goals





def main():
    
    result = {
        "items": []}
    intentions = get_intentions()
            
    for myIntention in intentions:
        if 'd' in myIntention:
                subString="✅ Completed"
                myArg = ""
        else:
            subString="↩️ to complete"
            myArg = myIntention['zid']


        result["items"].append({
                "title": myIntention['text'],
                "subtitle": subString,
                
                "valid":'TRUE',
                        
                "arg":myArg})
            

    print (json.dumps(result))

if __name__ == "__main__":
    main()