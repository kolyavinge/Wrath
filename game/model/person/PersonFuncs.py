from game.lib.Math import Math
from game.lib.Numeric import Numeric


class VelocityFunc:

    def getValue(self, time):
        return 0.2 * Math.ln(time + 1.0)


class JumpingFunc:

    def getValue(self, time):
        return Numeric.limitMax(0.5 * time, 0.2, 0.2)


class FallingFunc:

    def getValue(self, time):
        return 0.1 * time


class FallingDamageFunc:

    def getValue(self, time):
        if time < 2.5:
            return 0.0
        else:
            return 0.025 * time


class BreathFunc:

    def getValue(self, time):
        return 0.0015 * Math.sin(0.03 * time)
