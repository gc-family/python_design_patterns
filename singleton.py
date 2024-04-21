from pprint import pprint
from collections import *
from itertools import *
from functools import *


class Test:
    _singleton = None


class SinglTonClass(object):
    """docstring for SinglTonClass"""
    _singleton = None
    def __init__(self):
        super(SinglTonClass, self).__init__()
        pass

    def __new__(cls,*args,**kwargs):
        if not cls._singleton:
            cls._singleton=super(SinglTonClass,cls).__new__(cls,*args,**kwargs)

        return cls._singleton
        

if __name__ == '__main__':
    oop = SinglTonClass.__new__(SinglTonClass)
    oop2 = SinglTonClass()
    print(oop2)
    print(oop)
