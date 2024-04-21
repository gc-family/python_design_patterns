import gzip
import random
import socket
import time
from collections import deque
from io import BytesIO
import sys

FILE_NAME = 'test.txt'


class Observer:
    def __call__(self, *args, **kwargs):
        pass


class FirstObserver(Observer):
    def __init__(self, fileName):
        super(FirstObserver, self).__init__()
        self.fileName = fileName

    def __call__(self, *args, **kwargs):
        self.write_to_file(*args, **kwargs)

    def write_to_file(self, data):
        with open(self.fileName, mode='ab') as file:
            if type(data) == bytes:
                file.write(data)
            else:
                file.write(data.encode())


class SecondObserver(Observer):
    def __init__(self, fileName):
        super(SecondObserver, self).__init__()
        self.fileName = fileName

    def __call__(self, *args, **kwargs):
        self.write_to_stdout(*args, **kwargs)

    def write_to_stdout(self, data):
        if type(data) != bytes:
            self.fileName.write()
        else:
            self.fileName.write()


class CoreObserver:
    def __init__(self):
        self.observers = deque()
        self.inMessage = None

    @property
    def inMessage(self):
        return self._inMessage

    @inMessage.setter
    def inMessage(self, data):
        self._inMessage = data
        if self._inMessage is not None:
            if type(self._inMessage) == bytes:
                parameter = str(time.ctime()).encode() + self._inMessage
            else:
                parameter = time.ctime() + self._inMessage
            self.update(parameter)

    def attach(self, observer):
        print(callable(observer))
        if callable(observer):
            self.observers.append(observer)

    def update(self, *args, **kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)


class LogSocket:
    def __init__(self, sock):
        self._sock = sock

    def send(self, data):
        print("Sending {0} to {1}".format(data, self._sock.getpeername()[0]))
        self._sock.send(data)

    def close(self):
        self._sock.close()


class GzipSocket:
    def __init__(self, sock):
        self._sock = sock

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self._sock.send(buf.getvalue())

    def close(self):
        self._sock.close()


def respond(sock, observer):
    response = sock._sock.recv(124)
    observer.inMessage = response
    sock.send(bytes(response))
    print('sent : {}'.format(response))
    sock.close()


server = socket.socket()
server.bind(('localhost', 27493))
server.listen()


def main(server, observer):
    try:
        print("the server is listening on {}".format(('localhost', 27493)))
        while True:
            client, address = server.accept()
            print("created connection with {}".format(address))
            compressed = random.randint(0, 1)
            print(compressed)
            if not compressed:
                respond(LogSocket(client), observer)
            else:
                respond(GzipSocket(client), observer)

    except Exception:
        # print(types(e))
        raise

    finally:
        server.close()


if __name__ == '__main__':
    core = CoreObserver()
    core.attach(FirstObserver(FILE_NAME))
    core.attach(SecondObserver(sys.stdout))
    serverObj = main(server, core)
