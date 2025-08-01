from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Camera:

    def __init__(self):
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.verticalViewRadians = 0
        self.horizontalViewRadians = 0
        self.horizontalViewRadiansHalfCos = 0
        self.hasVerticalViewRadiansChanged = False

    def setVerticalViewRadians(self, verticalViewRadians):
        self.hasVerticalViewRadiansChanged = self.verticalViewRadians != verticalViewRadians
        self.verticalViewRadians = verticalViewRadians
        self.horizontalViewRadians = self.verticalViewRadians * CommonConstants.screenAspect
        self.horizontalViewRadiansHalfCos = Math.cos(self.horizontalViewRadians / 2.0)

    def calculateViewMatrix(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, CommonConstants.zAxis)

    def calculateProjectionMatrix(self):
        self.projectionMatrix.perspective(
            self.verticalViewRadians, CommonConstants.screenAspect, CommonConstants.minPerspectiveDepth, CommonConstants.maxPerspectiveDepth
        )
