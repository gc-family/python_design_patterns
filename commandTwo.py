import sys
import os


class Window:
    def __init__(self):
        self.message = "the window is Exiting"

    def exit(self):
        print(self.message)
        sys.exit(0)


class TextEditor:
    def __init__(self):
        self.data = None

    def create(self):
        print("this is CREATE function in from the textEditor")
        return 0

    def open(self):
        print("this is OPEN function in from the textEditor")
        return 0

    def close(self):
        print("this is CLOSE function in from the textEditor")
        return 0

    def copy(self, data):
        self.data = data
        print("this is COPY function in from the textEditor")
        return 0

    def cut(self):
        print("this is CUT function in from the textEditor")
        return 0


class Command:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class CreateCommand(Command):
    def __init__(self, editor):
        super(CreateCommand, self).__init__()
        self.editor = editor

    def __call__(self, *args, **kwargs):
        return self.editor.create(*args, **kwargs)


class OpenCommand(Command):
    def __init__(self, editor):
        super(OpenCommand, self).__init__()
        self.editor = editor

    def __call__(self, *args, **kwargs):
        return self.editor.open(*args, **kwargs)


class CloseCommand(Command):
    def __init__(self, editor):
        super(CloseCommand, self).__init__()
        self.editor = editor

    def __call__(self, *args, **kwargs):
        return self.editor.close(*args, **kwargs)


class CopyCommand(Command):
    def __init__(self, editor):
        super(CopyCommand, self).__init__()
        self.editor = editor

    def __call__(self, *args, **kwargs):
        return self.editor.copy(*args, **kwargs)


class CutCommand(Command):
    def __init__(self, editor):
        super(CutCommand, self).__init__()
        self.editor = editor

    def __call__(self, *args, **kwargs):
        return self.editor.cut(*args, **kwargs)


class ExitCommand(Command):
    def __init__(self, window):
        super(ExitCommand, self).__init__()
        self.windwo = window

    def __call__(self, *args, **kwargs):
        return self.windwo.exit(*args, **kwargs)


class InvokerBase:
    def __init__(self):
        self._command = None
        self._set = False

    def set_command(self, command):
        if self._set:
            raise Exception("first revoke : {} binding".format(self._command))
        else:
            self._command = command
            self._set = True

    def revoke_command(self):
        if self._set:
            self._command = None
            self._set = False
        else:
            raise Exception("First bound a callback or command")

    def click(self, *args, **kwargs):
        pass


class CreateButton(InvokerBase):
    def __init__(self):
        super(CreateButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        """you must call set_command with appropriate command->parameter"""
        return self._command(*args, **kwargs)


class OpenButton(InvokerBase):
    def __init__(self):
        super(OpenButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        return self._command(*args, **kwargs)


class CloseButton(InvokerBase):
    def __init__(self):
        super(CloseButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        return self._command(*args, **kwargs)


def fake_result():
    print("this is fake")


class CopyButton(InvokerBase):
    def __init__(self):
        super(CopyButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        return self._command(*args, **kwargs)


class CutButton(InvokerBase):
    def __init__(self):
        super(CutButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        return self._command(*args, **kwargs)


class ExitButton(InvokerBase):
    def __init__(self):
        super(ExitButton, self).__init__()
        pass

    def click(self, *args, **kwargs):
        return self._command(*args, **kwargs)


class Client:
    def __init__(self):
        self.__window = Window()
        self.__editor = TextEditor()
        self.__create_command = CreateCommand(self.__editor)
        self.__create_button = CreateButton()
        self.__create_button.set_command(fake_result)

    def create(self):
        return self.__create_button.click()


if __name__ == '__main__':
    user = Client()
    user.create()
