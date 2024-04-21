import sys
from collections import *
from itertools import *
from functools import *


class Light:
    """this is the Receiver Class"""

    def __init__(self):
        pass

    def On(self):
        print('turned the light On:')

    def Off(self):
        print('turned the light Off')


class Command:
    """the abstract class for the command class"""

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


def func_test(light):
    return light.On()


class TurnOnCommand(Command):
    def __init__(self, light):
        super(TurnOnCommand, self).__init__()
        self.light = light

    def __call__(self, *args, **kwargs):
        return self.light.On(*args, **kwargs)


class TurnOffCommand(Command):
    def __init__(self, light):
        super(TurnOffCommand, self).__init__()
        self.light = light

    def __call__(self, *args, **kwargs):
        return self.light.Off(*args, **kwargs)


class InvokerBase:
    """the invoker class"""

    def __init__(self):
        self.command = None
        self._set = False

    def set_command(self, command):
        if not self._set:
            self.command = command
            self._set = True
        else:
            raise Exception("error is occurred")

    def revoke_command(self):
        if self._set:
            self.command = None
            self._set = False
        else:
            raise Exception("this is not bound yet")


class Switch(InvokerBase):
    """the invoker class"""

    def __init__(self):
        super(Switch, self).__init__()
        pass

    def switchOn(self, *args, **kwargs):
        self.command(*args, **kwargs)

    def switchOff(self, *args, **kwargs):
        self.command(*args, **kwargs)


class ClientLight:
    def __init__(self):
        self.light = Light()
        self.onInvoker = Switch()
        self.onInvoker.set_command(lambda: func_test(self.light))
        self.offInvoker = Switch()
        self.offInvoker.set_command(TurnOffCommand(self.light))

    def turn_on(self):
        return self.onInvoker.switchOn()

    def turn_off(self):
        return self.offInvoker.switchOff()


if __name__ == '__main__':
    user = ClientLight()
    user.turn_on()
    user.turn_off()
