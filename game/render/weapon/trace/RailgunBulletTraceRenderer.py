from game.gl.ColorVector3 import ColorVector3
from game.render.anx.RayRenderer import RayParams
from game.render.weapon.trace.RayBulletTraceRenderer import RayBulletTraceRenderer


class RailgunBulletTraceRenderer:

    def __init__(self, rayBulletTraceRenderer):
        self.rayBulletTraceRenderer = rayBulletTraceRenderer
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.008
        self.rayParams.rayColor = ColorVector3(3, 252, 115)
        self.rayParams.rayColor.normalize()
        self.rayParams.shineStrength = 0.002

    def renderTrace(self, trace):
        self.rayBulletTraceRenderer.renderTrace(trace, self.rayParams)


def makeRailgunBulletTraceRenderer(resolver):
    return RailgunBulletTraceRenderer(resolver.resolve(RayBulletTraceRenderer))
