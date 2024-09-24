from game.anx.CommonConstants import CommonConstants
from game.model.level.Floor import Floor


class FlatFloor(Floor):

    def __init__(self):
        super().__init__()
        self.frontNormal = CommonConstants.up
        self.z = 0

    def getZ(self, x, y):
        return self.z

    def __str__(self):
        return f"({self.downLeft}),({self.downRight}),({self.upLeft}),({self.upRight})"
