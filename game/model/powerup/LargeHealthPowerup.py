from game.anx.PersonConstants import PersonConstants
from game.model.powerup.Powerup import Powerup
from game.model.powerup.PowerupKind import PowerupKind


class LargeHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.kind = PowerupKind.largeHealth
        self.value = int(PersonConstants.maxPersonHealth / 2)
        self.setRandomRotate()
        self.canCastShadow = True
