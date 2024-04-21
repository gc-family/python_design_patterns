from functools import *
from itertools import *
from collections import *
from PIL import Image
import abc
from abc import *


# print(dir(abc))
# this is simple observer pattern
class Inventory:
    def __init__(self):
        self.observers = []
        self._product  = None
        self._quantity = 0

    def __len__(self):
        return self.observers.__len__()

    def show(self):
        """display the available observers"""
        if self.observers:
            for obs in self.observers:
                print(obs)
        else:
            print("Empty")

    def attach(self,observer):
        self.observers.append(observer)

    def detach(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            raise ValueError

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self,value):
        self._product = value
        self.update_observers(self._product)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        self._quantity = value
        self.update_observers(self._quantity)

    def update_observers(self,*args,**kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)
            # observer.update(*args,**kwargs)

class SimpleObserver(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class UserOne(SimpleObserver):
    def __init__(self):
        pass    

    def __call__(self,*args,**kwargs):
        self.display_change(*args,**kwargs)

    def display_change(self,change):
        print("the change is : {}".format(change))

    def update(self, *args, **kwargs):
        self.display_change(*args,**kwargs)
        pass


if __name__ == '__main__':
    observer = Inventory()
    clientOne = UserOne()
    clientTwo = UserOne()
    observer.attach(clientTwo)
    observer.attach(clientOne)
    observer.quantity = 30