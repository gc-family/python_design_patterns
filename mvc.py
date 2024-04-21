
class Model:
    def __init__(self):
        pass

    def _database_connect(self):
        pass

    def parse_command(self,*args,**kwargs):
        pass

class DML(Model):
    def __init__(self):
        super(DML, self).__init__()
        pass

    def update(self,*args,**kwargs):
        pass

    def insert(self,*args,**kwargs):
        pass

    def delete(self,*args, **kwargs):
        pass


class DQL(Model):
    def __init__(self):
        super(DQL, self).__init__()
        pass

    def select(self,*args,**kwargs):
        pass


if __name__ == '__main__':
    pass