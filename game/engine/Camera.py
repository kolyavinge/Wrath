from game.calc.Vector3 import *
from game.calc.TranfsormMatrix4 import *
from game.calc.Geometry import *
from game.anx.Constants import *


class Camera:

    def __init__(self):
        self.viewAngleRadians = Geometry.degreesToRadians(60)
        self.position = Vector3()
        self.lookDirection = Vector3()
        self.lookPosition = Vector3()
        self.viewMatrix = TransformMatrix4()
        self.projectionMatrix = TransformMatrix4()
        self.projectionMatrix.perspective(self.viewAngleRadians, Constants.screenAspect, 0.1, Constants.maxDepth)

    def update(self):
        self.viewMatrix.lookAt(self.position, self.lookDirection, Constants.upDirection)

        return self.viewMatrix


def makeCamera(resolver):
    return Camera()
