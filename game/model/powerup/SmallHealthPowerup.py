from game.anx.CommonConstants import CommonConstants
from game.model.powerup.Powerup import Powerup


class SmallHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.value = int(CommonConstants.maxPersonHealth / 4)
        self.setRandomRotate()