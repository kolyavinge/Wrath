from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.ColorVector3 import ColorVector3
from game.render.anx.RayRenderer import RayParams, RayRenderer
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer


class RailgunBulletTraceRenderer:

    def __init__(self, rayRenderer, shineCircleRenderer):
        self.rayRenderer = rayRenderer
        self.shineCircleRenderer = shineCircleRenderer
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.001
        self.rayParams.rayColor = ColorVector3(3, 252, 115)
        self.rayParams.rayColor.normalize()
        self.rayParams.shineStrength = 0.002
        self.shineCircleParams = ShineCircleParams()
        self.shineCircleParams.radius = 0.005
        self.shineCircleParams.shineColor = self.rayParams.rayColor
        self.shineCircleParams.shineStrength = self.rayParams.shineStrength

    def renderTrace(self, trace):
        self.rayRenderer.render(trace.startPosition, trace.currentPosition, self.rayParams)
        modelMatrix = TransformMatrix4()
        modelMatrix.translate(trace.startPosition.x, trace.startPosition.y, trace.startPosition.z)
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams)


def makeRailgunBulletTraceRenderer(resolver):
    return RailgunBulletTraceRenderer(resolver.resolve(RayRenderer), resolver.resolve(ShineCircleRenderer))
