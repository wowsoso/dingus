#!/usr/bin/env python

from dingus import Dingus, patch, isolate
from nose.tools import *

def init_user(*args):
    raise Exception("error")

def get_cur_influence(*args):
    raise Exception("error")    

def get_last_influence(*args):
    raise Exception("error")    

class db():
    def __init__(self):
        raise Exception("error")


def get_user(uid, user_data=None):
    init_user(uid, user_data)
    resultdict = db.users.find_one({'_id': uid})
    influence = get_cur_influence(uid)
    if not influence.get('followers_count', 0):
        influence = get_last_influence(uid)
        resultdict['friends_count'] = influence.get('friends_count', 0)
        resultdict['followers_count'] = influence.get('followers_count', 0)
        resultdict['statuses_count'] = influence.get('statuses_count', 0)
        resultdict['influence'] = influence.get('influence', 0)
    return resultdict



# @patch('test_get_user.init_user', lambda x, y: None)
# @patch('test_get_user.db', Dingus(users=Dingus(find_one__returns={})))
# @patch('test_get_user.get_cur_influence', lambda x: {})
# @patch('test_get_user.get_last_influence', lambda x: {})
def test_get_user():
    dic = get_user(1, None)
    assert dic["friends_count"] == 0

