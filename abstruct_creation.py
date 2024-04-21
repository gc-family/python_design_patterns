import abc
import sys


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class Ogg(MediaLoader):
    ext = '.oog'

    def play(self):
        pass

if __name__ ==  '__main__':
    waveFile = Ogg()
    print(Ogg is MediaLoader)
