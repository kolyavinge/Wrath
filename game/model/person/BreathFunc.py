from game.lib.Math import Math


class BreathFunc:

    def getValue(self, time):
        return 0.0015 * Math.sin(0.03 * time)
