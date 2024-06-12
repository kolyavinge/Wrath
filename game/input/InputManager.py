from game.lib.Screen import Screen
from game.input.Mouse import Mouse
from game.input.Keyboard import Keyboard


class InputManager:

    def __init__(self):
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        self.mouse = Mouse()
        self.mouse.setInitCursorPosition(screenWidth / 2, screenHeight / 2)
        self.keyboard = Keyboard()

    def update(self):
        self.mouse.update()
        self.keyboard.update()


def makeInputManager(resolver):
    return InputManager()
