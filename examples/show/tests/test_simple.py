#!/usr/bin/env python

from dingus import Dingus
from nose.tools import *

def read_socket(socket):
    data = socket.recv(1024)
    socket.close()
    return data

def test_read_socket():
    socket = Dingus(recv__returns="blablabla")
    assert_equals("blablabla", read_socket(socket))


def bad_read_socket():
    data = socket.recv(1024)
    socket.close()
    return data


def test_bad_read_socket():
    global socket
    socket = Dingus(recv__returns="blablabla")
    assert_equals("blablabla", bad_read_socket())
    del socket
