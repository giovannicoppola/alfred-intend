#!/usr/bin/python3 
# encoding: utf-8
### python script to interact with Complice
### giovanni, Saturday, April 10, 2021, 2:11 PM
### March 2022 updated to Python 3


import sys
from config import POMOLENGTH, TIMERLENGTH, TOKEN
import complice_post

    



myInput = sys.argv[1]

if myInput == "startTimer":
    complice_post.start_hourglass()


if myInput == "startPomo":
    complice_post.start_pomo()
    

if myInput == "Timer30":
    complice_post.start_custom_hourglass30()
    
if myInput == "Timer60":
    complice_post.start_custom_hourglass60()

if myInput == "runningTimerPause":
    complice_post.pause_timer()

if myInput == "runningTimerCancel":
    complice_post.cancel_timer()

if myInput == "pausedTimerCancel":
    complice_post.cancel_timer()


if myInput == "restartTimer":
    complice_post.restart_hourglass()

if myInput == "runningPomo":
    complice_post.cancel_timer()

if myInput == "breaking":
    complice_post.cancel_timer()

