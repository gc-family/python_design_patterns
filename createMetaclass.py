className = "Foo"
classParents = (object,)
classBody = """
def __init(self,x):
    self.x = x
def blah(self):
    print("hello world")
"""

classDict = {}
# Execute the body in the local dictionary class_dict
exec(classBody,globals(),classDict)

Foo = type(className,classParents,classDict)


class DocMeta(type):
    def __init__(self,name,bases,dict):
        for key, value in dict.items():
            # Skip special and private methods
            if key.startswith("__"): continue
            # Skip anything not callable
            if not hasattr(value,"__call__"): continue
            # Check for a doc-string
            if not getattr(value,"__doc__"):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self,name,bases,dict)


# class Documented:
#     __metaclass__ = DocMeta

class Documented(metaclass=DocMeta):
    pass


class Foo(Documented):
    def spam(self,a,b):
        """spam does something"""
        pass

if __name__ == '__main__':
    f = Foo()
    print(dir(f))
    print(type(f))
    print(f.__class__.spam.__dict__)
