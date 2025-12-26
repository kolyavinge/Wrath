from game.gl.ColorVector3 import ColorVector3
from game.lib.Query import Query
from game.render.anx.PlaneRayRenderer import RayParams
from game.render.weapon.trace.RayBulletTraceRenderer import RayBulletTraceRenderer


class RailgunBulletTraceRenderer:

    def __init__(self, rayBulletTraceRenderer: RayBulletTraceRenderer):
        self.rayBulletTraceRenderer = rayBulletTraceRenderer
        self.defaultRayColor = ColorVector3(3, 252, 115)
        self.defaultRayColor.normalize()
        self.chargedRayColor = ColorVector3(252, 3, 115)
        self.chargedRayColor.normalize()
        self.rayParams = RayParams()
        self.rayParams.rayHeight = 0.008
        self.rayParams.rayColor = self.defaultRayColor
        self.rayParams.shineStrength = 0.002

    def renderTraces(self, traces):
        charged, notCharged = Query(traces).split(lambda trace: trace.bullet.isCharged)

        if len(notCharged) > 0:
            self.rayBulletTraceRenderer.renderTraces(notCharged, self.rayParams)

        if len(charged) > 0:
            self.rayParams.rayColor = self.chargedRayColor
            self.rayBulletTraceRenderer.renderTraces(charged, self.rayParams)
            self.rayParams.rayColor = self.defaultRayColor
