class PowerupIdLogic:

    def __init__(self):
        self.lastPowerupId = 1

    def getPowerupId(self):
        result = self.lastPowerupId
        self.lastPowerupId += 1

        return result
