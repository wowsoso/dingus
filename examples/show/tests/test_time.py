#!/usr/bin/env python

import time
from dingus import Dingus
from nose.tools import *

def foo():
    time.sleep(.2)

def test_time():
    timed(.3)(foo)()
