class ExplosionIdLogic:

    def __init__(self):
        self.lastExplosionId = 0

    def getExplosionId(self):
        self.lastExplosionId += 1

        return self.lastExplosionId
