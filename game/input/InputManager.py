from game.input.Cursor import Cursor
from game.input.Keyboard import Keyboard


class InputManager:

    def __init__(self):
        self.cursor = Cursor()
        self.keyboard = Keyboard()

    def update(self):
        pass


def makeInputManager(resolver):
    return InputManager()
