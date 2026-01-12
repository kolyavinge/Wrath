from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Camera:

    def __init__(self):
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.viewProjectionMatrix = TransformMatrix4()
        self.verticalViewRadians = 0
        self.horizontalViewRadians = 0
        self.hasVerticalViewRadiansChanged = False

    def setVerticalViewRadians(self, verticalViewRadians):
        self.hasVerticalViewRadiansChanged = self.verticalViewRadians != verticalViewRadians
        self.verticalViewRadians = verticalViewRadians
        self.horizontalViewRadians = self.verticalViewRadians * CommonConstants.screenAspect

    def calculateViewMatrix(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, CommonConstants.zAxis)

    def calculateProjectionMatrix(self):
        self.projectionMatrix.perspective(
            self.verticalViewRadians, CommonConstants.screenAspect, CommonConstants.minPerspectiveDepth, CommonConstants.maxPerspectiveDepth
        )

    def calculateProjectionViewMatrix(self):
        newViewProjectionMatrix = self.projectionMatrix.copy()
        newViewProjectionMatrix.mul(self.viewMatrix)
        self.viewProjectionMatrix = newViewProjectionMatrix

    def getCameraFacedNormal(self, pointInWorld):
        normal = pointInWorld.getDirectionTo(self.position)
        normal.normalize()

        return normal
