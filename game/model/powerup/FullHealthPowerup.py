from game.anx.CommonConstants import CommonConstants
from game.model.powerup.Powerup import Powerup


class FullHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.height = 0.2
        self.value = CommonConstants.maxPersonHealth