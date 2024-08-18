from game.lib.Math import Math


class VelocityFunc:

    def __init__(self):
        self.forwardMaxTime = 1.5
        self.backwardMaxTime = 0.5

    def getValue(self, time):
        return Math.ln(time + 1)
