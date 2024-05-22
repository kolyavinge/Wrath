class Cursor:

    def __init__(self, centerX, centerY):
        self.x = centerX
        self.y = centerY
        self.dx = 0
        self.dy = 0

    def setPosition(self, x, y):
        self.dx = x - self.x
        self.dy = y - self.y

    def reset(self):
        self.dx = 0
        self.dy = 0
