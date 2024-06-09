from game.input.Mouse import Mouse
from game.input.Keyboard import Keyboard


class InputManager:

    def __init__(self):
        self.mouse = Mouse()
        self.keyboard = Keyboard()

    def update(self):
        pass


def makeInputManager(resolver):
    return InputManager()
