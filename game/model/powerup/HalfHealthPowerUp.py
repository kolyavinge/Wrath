from game.anx.CommonConstants import CommonConstants
from game.model.powerup.PowerUp import PowerUp


class HalfHealthPowerUp(PowerUp):

    def __init__(self):
        super().__init__()
        self.height = 0.2
        self.value = int(CommonConstants.maxPersonHealth / 2)
