from game.input.Keyboard import Keyboard
from game.input.Mouse import Mouse
from game.lib.Screen import Screen


class InputManager:

    def __init__(self):
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        self.mouse = Mouse()
        self.mouse.setInitCursorPosition(screenWidth / 2, screenHeight / 2)
        self.keyboard = Keyboard()

    def update(self):
        if Screen.isFocused():
            self.mouse.update()
            self.keyboard.update()
