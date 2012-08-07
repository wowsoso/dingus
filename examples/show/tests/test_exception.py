#!/usr/bin/env python

from dingus import Dingus
from nose.tools import *


def foo():
    raise Exception("error")        

@raises(Exception)
def test_exception():
    foo()
