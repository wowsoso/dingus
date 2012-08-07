#!/usr/bin/env python

from dingus import Dingus
from nose.tools import *

def foo(func, flag):
    if flag:
        func()
        func()
    else:
        func()

def test_proc_count():
    dingus = Dingus()
    foo(dingus.func, True)
    assert len(dingus.calls('func')) == 2

    dingus = Dingus()
    foo(dingus.func, False)
    assert len(dingus.calls('func')) == 1
