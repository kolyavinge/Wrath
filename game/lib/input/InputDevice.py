class ButtonState:

    released = 0
    pressed = 1
    held = 2
    lifted = 3


class InputDevice:

    def __init__(self, allButtons):
        self.allButtons = allButtons
        self.buttonStates = {}
        for button in allButtons:
            self.buttonStates[button] = ButtonState.released

    def update(self):
        for button in self.allButtons:
            pressed = self.checkInnerPressed(button)
            if self.buttonStates[button] == ButtonState.released and pressed:
                self.buttonStates[button] = ButtonState.pressed
            elif self.buttonStates[button] == ButtonState.pressed and pressed:
                self.buttonStates[button] = ButtonState.held
            elif self.buttonStates[button] == ButtonState.pressed and not pressed:
                self.buttonStates[button] = ButtonState.lifted
            elif self.buttonStates[button] == ButtonState.held and not pressed:
                self.buttonStates[button] = ButtonState.lifted
            elif self.buttonStates[button] == ButtonState.lifted and not pressed:
                self.buttonStates[button] = ButtonState.released

    def isReleased(self, button):
        return self.buttonStates[button] == ButtonState.released

    def isPressed(self, button):
        return self.buttonStates[button] == ButtonState.pressed

    def isHeld(self, button):
        return self.buttonStates[button] == ButtonState.held

    def isPressedOrHeld(self, button):
        return self.isPressed(button) or self.isHeld(button)

    def isLifted(self, button):
        return self.buttonStates[button] == ButtonState.lifted

    def checkInnerPressed(self, button):
        pass
