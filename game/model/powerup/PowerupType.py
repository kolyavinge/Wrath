from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.PowerupKind import PowerupKind
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupType:

    @staticmethod
    def getPowerupTypeFromKind(kind):
        if PowerupKind.isWeaponPowerup(kind):
            return WeaponPowerup
        else:
            types = {
                PowerupKind.largeHealth: LargeHealthPowerup,
                PowerupKind.smallHealth: SmallHealthPowerup,
                PowerupKind.vest: VestPowerup,
            }

            return types[kind]
