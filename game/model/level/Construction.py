from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.model.Material import Material


class Construction:

    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.frontNormal = CommonConstants.up
        self.material = Material.blank

    def getBorderPoints(self):
        return [self.downLeft, self.downRight, self.upLeft, self.upRight]
