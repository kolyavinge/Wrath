from game.lib.Math import Math


class VelocityFunc:

    def getValue(self, time):
        return Math.ln(time + 1) / 8
