import keyboard

from game.input.Keys import Keys


class KeyState:
    released = 0
    pressed = 1
    held = 2


class Keyboard:

    def __init__(self):
        self.keyStates = {}
        for key in Keys.allKeys:
            self.keyStates[key] = KeyState.released

    def update(self):
        for key in Keys.allKeys:
            pressed = keyboard.is_pressed(key)
            if self.keyStates[key] == KeyState.released and pressed:
                self.keyStates[key] = KeyState.pressed
            elif self.keyStates[key] == KeyState.pressed and pressed:
                self.keyStates[key] = KeyState.held
            elif self.keyStates[key] == KeyState.held and not pressed:
                self.keyStates[key] = KeyState.released
            elif self.keyStates[key] == KeyState.pressed and not pressed:
                self.keyStates[key] = KeyState.released

    def isReleased(self, key):
        return self.keyStates[key] == KeyState.released

    def isPressed(self, key):
        return self.keyStates[key] == KeyState.pressed

    def isHeld(self, key):
        return self.keyStates[key] == KeyState.held

    def isPressedOrHeld(self, key):
        return self.isPressed(key) or self.isHeld(key)
