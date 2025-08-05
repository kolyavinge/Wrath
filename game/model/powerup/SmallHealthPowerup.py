from game.anx.PersonConstants import PersonConstants
from game.model.powerup.Powerup import Powerup


class SmallHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.value = int(PersonConstants.maxPersonHealth / 4)
        self.setRandomRotate()
        self.canCastShadow = True
