#!/usr/bin/env python
# encoding: utf-8
#
#
# Sunday, April 11, 2021, 11:01 AM
#

"""Common settings."""

from __future__ import unicode_literals
import os
from workflow import Workflow3, ICON_WARNING

wf = Workflow3()

POMOLENGTH = os.path.expanduser(os.getenv('POMOLENGTH', ''))
TIMERLENGTH = os.path.expanduser(os.getenv('TIMERLENGTH', ''))
TOKEN = os.path.expanduser(os.getenv('TOKEN', ''))
    

	
