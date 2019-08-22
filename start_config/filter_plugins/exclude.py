#!/usr/bin/python

from builtins import object
from ansible import errors

def exclude(a, b):
    temp = a.copy()
    if isinstance(a,dict):
        temp.pop(b, None)
    return temp
class FilterModule(object):
    def filters(self):
        return {
            'exclude': exclude
        }