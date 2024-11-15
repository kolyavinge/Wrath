from game.model.powerup.Powerup import Powerup


class VestPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.setRandomRotate()
