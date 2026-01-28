class PowerupIdLogic:

    def __init__(self):
        self.lastPowerupId = 0

    def getPowerupId(self):
        self.lastPowerupId += 1

        return self.lastPowerupId
