class PowerupKind:

    unknown = 0

    # numbers from 1 to 6 reserved for weapons

    largeHealth = 100
    smallHealth = 101
    vest = 102

    @staticmethod
    def isWeaponPowerup(kind):
        return PowerupKind.unknown < kind and kind < PowerupKind.largeHealth
