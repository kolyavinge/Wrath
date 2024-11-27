from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder


class Flash:

    def __init__(self):
        self.weaponType = None
        self.alpha = 0
        self.isVisible = True

    def update(self):
        pass

    def calculateModelMatrix(self, position, yawRadians, pitchRadians):
        self.modelMatrix = (
            TransformMatrix4Builder()
            .translate(position.x, position.y, position.z)
            .rotate(yawRadians, CommonConstants.zAxis)
            .rotate(pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )

    def getModelMatrix(self):
        return self.modelMatrix
