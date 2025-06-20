from game.gl.ColorVector3 import ColorVector3
from game.render.anx.RayRenderer import RayParams
from game.render.weapon.trace.RayBulletTraceRenderer import RayBulletTraceRenderer


class RifleBulletTraceRenderer:

    def __init__(self, rayBulletTraceRenderer: RayBulletTraceRenderer):
        self.rayBulletTraceRenderer = rayBulletTraceRenderer
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.0005
        self.rayParams.rayColor = ColorVector3(100, 100, 100)
        self.rayParams.rayColor.normalize()
        self.rayParams.shineStrength = 0

    def renderTrace(self, trace):
        self.rayBulletTraceRenderer.renderTrace(trace, self.rayParams)
