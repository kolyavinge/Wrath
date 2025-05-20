from game.lib.Math import Math


class VelocityFunc:

    def getValue(self, time):
        return Math.ln(time + 1.0) / 5.0


class FallingFunc:

    def getValue(self, x):
        return 2.0 * x


class BreathFunc:

    def getValue(self, time):
        return 0.0015 * Math.sin(0.03 * time)
