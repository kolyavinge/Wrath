from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Camera:

    def __init__(self):
        self.verticalViewDegrees = 45
        self.verticalViewRadians = Geometry.degreesToRadians(self.verticalViewDegrees)
        self.horizontalViewRadians = self.verticalViewRadians * CommonConstants.screenAspect
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.projectionMatrix.perspective(
            self.verticalViewRadians, CommonConstants.screenAspect, CommonConstants.minPerspectiveDepth, CommonConstants.maxPerspectiveDepth
        )

    def calculateViewMatrix(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, CommonConstants.zAxis)
