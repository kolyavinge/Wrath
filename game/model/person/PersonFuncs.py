from game.lib.Math import Math
from game.lib.Numeric import Numeric


class VelocityFunc:

    def getValue(self, time):
        return 0.4 * Math.ln(time + 1.0)


class JumpingFunc:

    def getValue(self, time):
        return Numeric.limitMax(1.0 * time, 0.2, 0.2)


class FallingFunc:

    def getValue(self, time):
        return 0.4 * time


class FallingDamageFunc:

    def getValue(self, time):
        if time < 1.0:
            return 0.0
        else:
            return 0.04 * time


class BreathFunc:

    def getValue(self, time):
        return 0.002 * Math.sin(0.06 * time)
