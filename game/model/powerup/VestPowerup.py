from game.model.powerup.Powerup import Powerup
from game.model.powerup.PowerupKind import PowerupKind


class VestPowerup(Powerup):

    def __init__(self, kind=None):
        assert kind is None or kind == PowerupKind.vest
        super().__init__()
        self.kind = PowerupKind.vest
        self.setRandomRotate()
        self.canCastShadow = True
