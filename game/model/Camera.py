from game.anx.Constants import Constants
from game.calc.Geometry import Geometry
from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Camera:

    def __init__(self):
        self.viewAngleDegrees = 45
        self.viewAngleRadians = Geometry.degreesToRadians(self.viewAngleDegrees)
        self.viewAngleRadiansHalf = self.viewAngleRadians / 2
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.projectionMatrix.perspective(self.viewAngleRadians, Constants.screenAspect, Constants.minDepth, Constants.maxDepth)

    def calculateViewMatrix(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, Constants.zAxis)
