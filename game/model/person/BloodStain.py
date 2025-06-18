from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3


class BloodStain:

    numbersCount = 1

    def __init__(self):
        self.number = 0
        self.position = Vector3()
        self.brightness = 0
        self.fade = 0
        self.radians = 0
        self.scaleVector = Vector3()

    def getModelMatrix(self, viewportWidth, viewportHeight):
        return (
            TransformMatrix4Builder()
            .translate(self.position.x * viewportWidth, self.position.y * viewportHeight, self.position.z)
            .rotate(self.radians, CommonConstants.zAxis)
            .scale(self.scaleVector.x, self.scaleVector.y, self.scaleVector.z)
            .resultMatrix
        )
