from game.anx.PersonConstants import PersonConstants
from game.model.powerup.Powerup import Powerup


class LargeHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.value = int(PersonConstants.maxPersonHealth / 2)
        self.setRandomRotate()
