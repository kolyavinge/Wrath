from OpenGL.GL import *

from game.gl.ColorVector3 import ColorVector3
from game.render.anx.RayRenderer import RayParams, RayRenderer


class RifleBulletTraceRenderer:

    def __init__(self, rayRenderer):
        self.rayRenderer = rayRenderer
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.002
        self.rayParams.rayColor = ColorVector3(100, 100, 100)
        self.rayParams.rayColor.normalize()
        self.rayParams.shineStrength = 0

    def renderTrace(self, trace):
        self.rayParams.rayBrightness = trace.brightness
        self.rayRenderer.render(trace.startPosition, trace.currentPosition, self.rayParams)


def makeRifleBulletTraceRenderer(resolver):
    return RifleBulletTraceRenderer(resolver.resolve(RayRenderer))
