class Cursor:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    def setPosition(self, x, y):
        self.dx = x - self.x
        self.dy = y - self.y

    def reset(self):
        self.dx = 0
        self.dy = 0
