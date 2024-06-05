from game.input.Cursor import Cursor


class InputManager:

    def __init__(self):
        self.cursor = Cursor()

    def update(self):
        pass


def makeInputManager(resolver):
    return InputManager()
