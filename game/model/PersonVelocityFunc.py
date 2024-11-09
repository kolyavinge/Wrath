from game.lib.Math import Math


class PersonVelocityFunc:

    def getValue(self, time):
        return Math.ln(time + 1) / 2
