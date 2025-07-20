from game.anx.CommonConstants import CommonConstants
from game.model.level.Construction import Construction


class Floor(Construction):

    def __init__(self):
        super().__init__()
        self.frontNormal = CommonConstants.up
        self.visualSize = 2.0

    def commit(self):
        super().commit()

    def getZ(self, x, y):
        return self.plane.getZ(x, y)
