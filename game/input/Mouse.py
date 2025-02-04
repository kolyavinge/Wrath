import mouse


class Mouse:

    def __init__(self):
        self.initX = 0
        self.initY = 0
        self.dx = 0
        self.dy = 0
        self.scrollDelta = 0
        self.scrollDeltaRequest = 0
        self.leftButtonPressed = False
        self.leftButtonPressedRequest = False
        self.rightButtonClicked = False
        self.rightButtonClickedRequest = False
        self.rightButtonPressed = False
        self.rightButtonPressedRequest = False
        mouse.on_button(self.onLeftButtonPressed, (), mouse.LEFT, (mouse.DOWN, mouse.DOUBLE))
        mouse.on_button(self.onLeftButtonReleased, (), mouse.LEFT, mouse.UP)
        mouse.on_right_click(self.onRightButtonClicked, ())
        mouse.on_button(self.onRightButtonPressed, (), mouse.RIGHT, (mouse.DOWN, mouse.DOUBLE))
        mouse.on_button(self.onRightButtonReleased, (), mouse.RIGHT, mouse.UP)
        mouse.hook(self.onScroll)

    def setInitCursorPosition(self, x, y):
        self.initX = x
        self.initY = y

    def update(self):
        x, y = mouse.get_position()
        self.dx = x - self.initX
        self.dy = y - self.initY
        self.resetCursorPosition()
        self.leftButtonPressed = self.leftButtonPressedRequest
        self.rightButtonClicked = self.rightButtonClickedRequest
        self.rightButtonPressed = self.rightButtonPressedRequest
        self.rightButtonClickedRequest = False
        self.scrollDelta = self.scrollDeltaRequest
        self.scrollDeltaRequest = 0

    def isLeftButtonPressed(self):
        return self.leftButtonPressed

    def isRightButtonClicked(self):
        return self.rightButtonClicked

    def isRightButtonPressed(self):
        return self.rightButtonPressed

    def getScrollDelta(self):
        return self.scrollDelta

    def resetCursorPosition(self):
        mouse.move(self.initX, self.initY)

    def onLeftButtonPressed(self):
        self.leftButtonPressedRequest = True

    def onLeftButtonReleased(self):
        self.leftButtonPressedRequest = False

    def onRightButtonClicked(self):
        self.rightButtonClickedRequest = True

    def onRightButtonPressed(self):
        self.rightButtonPressedRequest = True

    def onRightButtonReleased(self):
        self.rightButtonPressedRequest = False

    def onScroll(self, a):
        if type(a) == mouse.WheelEvent:
            self.scrollDeltaRequest = a.delta
