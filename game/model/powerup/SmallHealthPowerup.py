from game.anx.PersonConstants import PersonConstants
from game.model.powerup.Powerup import Powerup
from game.model.powerup.PowerupKind import PowerupKind


class SmallHealthPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.kind = PowerupKind.smallHealth
        self.value = int(PersonConstants.maxPersonHealth / 4)
        self.setRandomRotate()
        self.canCastShadow = True
