from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Camera:

    def __init__(self):
        self.viewAngleDegrees = 45
        self.viewAngleRadians = Geometry.degreesToRadians(self.viewAngleDegrees)
        self.viewAngleRadiansHalf = self.viewAngleRadians / 2
        self.viewAngleRadiansQuarter = self.viewAngleRadians / 4
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.projectionMatrix.perspective(self.viewAngleRadians, CommonConstants.screenAspect, CommonConstants.minDepth, CommonConstants.maxDepth)

    def calculateViewMatrix(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, CommonConstants.zAxis)
