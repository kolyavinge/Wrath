from game.anx.PersonConstants import PersonConstants
from game.model.powerup.Powerup import Powerup
from game.model.powerup.PowerupKind import PowerupKind


class LargeHealthPowerup(Powerup):

    def __init__(self, kind=None):
        assert kind is None or kind == PowerupKind.largeHealth
        super().__init__()
        self.kind = PowerupKind.largeHealth
        self.value = int(PersonConstants.maxPersonHealth / 2)
        self.setRandomRotate()
        self.canCastShadow = True
