import mouse


class Mouse:

    def __init__(self):
        self.initX = 0
        self.initY = 0
        self.dx = 0
        self.dy = 0

    def setInitCursorPosition(self, x, y):
        self.initX = x
        self.initY = y

    def update(self):
        x, y = mouse.get_position()
        self.dx = x - self.initX
        self.dy = y - self.initY
        self.resetCursorPosition()

    def resetCursorPosition(self):
        mouse.move(self.initX, self.initY)
