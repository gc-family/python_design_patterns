class Duck(object):
    """docstring for Duck"""

    def __init__(self):
        super(Duck, self).__init__()
        self.flyBehavior = FlyBehavior()
        self.quackBehavior = QuackBehavior()

    def swim(self):
        print("All ducks float, even decoys")

    def display(self):
        print("this is default display for all types of duck")

    def setFlyBehavior(self, flyBehavior):
        assert isinstance(flyBehavior, FlyBehavior)
        self.flyBehavior = flyBehavior

    def setQuackBehavior(self, quackBehavior):
        assert isinstance(quackBehavior, QuackBehavior)
        self.quackBehavior = quackBehavior

    def performFly(self):
        return self.flyBehavior.fly()

    def performQuack(self):
        return self.quackBehavior.quack()


class MallardDuck(Duck):
    """docstring for MallardDuck"""

    def __init__(self):
        super(MallardDuck, self).__init__()
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()
        pass

    def display(self):
        print("I am real Mallard duck")


class ModelDuck(Duck):
    """docstring for ModelDuck"""

    def __init__(self):
        super(ModelDuck, self).__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyNoWay()
        pass

    def display(self):
        print("I am Model Duck")


class ReadHeadDuck(Duck):
    """docstring for ReadHeadDuck"""

    def __init__(self):
        super(ReadHeadDuck, self).__init__()
        pass


class DecoyDuck(Duck):
    """docstring for DecoyDuck"""

    def __init__(self):
        super(DecoyDuck, self).__init__()
        pass


class RubberDuck(Duck):
    """docstring for RubberDuck"""

    def __init__(self):
        super(RubberDuck, self).__init__()
        pass


# interfaces

class FlyBehavior(object):
    """Interface for FlyBehavior"""

    def __init__(self):
        super(FlyBehavior, self).__init__()
        pass

    def fly(self):
        pass


class QuackBehavior(object):
    """Interface for QuackBehavior"""

    def __init__(self):
        super(QuackBehavior, self).__init__()
        pass

    def quack(self):
        pass


# implementation
class FlyWithWings(FlyBehavior):
    """docstring for FlyWithWings"""

    def __init__(self):
        super(FlyWithWings, self).__init__()
        pass

    def fly(self):
        print("I am flying!!")


class FlyNoWay(FlyBehavior):
    """docstring for FlyNoWay"""

    def __init__(self):
        super(FlyNoWay, self).__init__()
        pass

    def fly(self):
        print("I can't Fly")


class FlyRocketPowered(FlyBehavior):
    """docstring for FlyRocketPowered"""

    def __init__(self):
        super(FlyRocketPowered, self).__init__()
        pass

    def fly(self):
        print("I am flying with rocket!!")


class Quack(QuackBehavior):
    """docstring for Quack"""

    def __init__(self):
        super(Quack, self).__init__()
        pass

    def quack(self):
        print("Quack!!")


class Squeak(QuackBehavior):
    """docstring for Squeak"""

    def __init__(self):
        super(Squeak, self).__init__()
        pass

    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):
    """docstring for MuteQuack"""

    def __init__(self):
        super(MuteQuack, self).__init__()
        pass

    def quack(self):
        print("<< silence >>")


class MiniDuckSimulator(object):
    def __init__(self):
        super(__class__, self).__init__()
        self.mallard = MallardDuck()
        self.mallard.performFly()
        self.mallard.performQuack()
        self.mallard.display()

        # self.model = ModelDuck()
        # self.model.performFly()
        # self.model.setFlyBehavior(FlyRocketPowered())
        # self.model.performFly()
        # self.model.display()


if __name__ == '__main__':
    test = MiniDuckSimulator()
