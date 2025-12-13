import mouse

from game.input.InputDevice import InputDevice


class MouseButtons:

    left = "left"
    right = "right"

    allButtons = [left, right]


class Mouse(InputDevice):

    def __init__(self):
        super().__init__(MouseButtons.allButtons)
        self.initX = 0
        self.initY = 0
        self.dx = 0
        self.dy = 0
        self.scrollDelta = 0
        self.scrollDeltaRequest = 0
        self.leftButtonPressed = False
        self.rightButtonPressed = False
        mouse.on_button(self.onLeftButtonPressed, (), mouse.LEFT, (mouse.DOWN, mouse.DOUBLE))
        mouse.on_button(self.onLeftButtonReleased, (), mouse.LEFT, mouse.UP)
        mouse.on_button(self.onRightButtonPressed, (), mouse.RIGHT, (mouse.DOWN, mouse.DOUBLE))
        mouse.on_button(self.onRightButtonReleased, (), mouse.RIGHT, mouse.UP)
        mouse.hook(self.onScroll)

    def onLeftButtonPressed(self):
        self.leftButtonPressed = True

    def onLeftButtonReleased(self):
        self.leftButtonPressed = False

    def onRightButtonPressed(self):
        self.rightButtonPressed = True

    def onRightButtonReleased(self):
        self.rightButtonPressed = False

    def checkInnerPressed(self, button):
        if button == MouseButtons.left:
            return self.leftButtonPressed
        elif button == MouseButtons.right:
            return self.rightButtonPressed
        else:
            return False

    def setInitCursorPosition(self, x, y):
        self.initX = x
        self.initY = y

    def update(self):
        super().update()
        x, y = mouse.get_position()
        self.dx = x - self.initX
        self.dy = y - self.initY
        self.resetCursorPosition()
        self.scrollDelta = self.scrollDeltaRequest
        self.scrollDeltaRequest = 0

    def resetCursorPosition(self):
        mouse.move(self.initX, self.initY)

    def onScroll(self, a):
        if type(a) == mouse.WheelEvent:
            self.scrollDeltaRequest = a.delta
