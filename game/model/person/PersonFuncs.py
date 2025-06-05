from game.lib.Math import Math


class VelocityFunc:

    def getValue(self, time):
        return Math.ln(time + 1.0) / 2.5


class JumpingFunc:

    def getValue(self, x):
        return 0.5 * x


class FallingFunc:

    def getValue(self, x):
        return 0.2 * x


class BreathFunc:

    def getValue(self, time):
        return 0.0015 * Math.sin(0.03 * time)
