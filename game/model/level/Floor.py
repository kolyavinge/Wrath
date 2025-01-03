from game.anx.CommonConstants import CommonConstants
from game.model.level.Construction import Construction


class Floor(Construction):

    def __init__(self):
        super().__init__()
        self.frontNormal = CommonConstants.up

    def commit(self):
        super().commit()
        # assert self.plane.c != 0

    def getZ(self, x, y):
        return self.plane.getZ(x, y)
