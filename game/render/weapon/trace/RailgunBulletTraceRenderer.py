from OpenGL.GL import *

from game.gl.ColorVector3 import ColorVector3
from game.render.anx.RayRenderer import RayParams, RayRenderer


class RailgunBulletTraceRenderer:

    def __init__(self, rayRenderer):
        self.rayRenderer = rayRenderer
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.008
        self.rayParams.rayColor = ColorVector3(3, 252, 115)
        self.rayParams.rayColor.normalize()
        self.rayParams.shineStrength = 0.002

    def renderTrace(self, trace):
        self.rayParams.rayBrightness = trace.brightness
        self.rayRenderer.render(trace.startPosition, trace.currentPosition, self.rayParams)


def makeRailgunBulletTraceRenderer(resolver):
    return RailgunBulletTraceRenderer(resolver.resolve(RayRenderer))
