from game.render.anx.RayRenderer import RayRenderer


class RayBulletTraceRenderer:

    def __init__(self, rayRenderer):
        self.rayRenderer = rayRenderer

    def renderTrace(self, trace, rayParams):
        rayParams.rayBrightness = trace.brightness
        self.rayRenderer.render(trace.startPosition, trace.currentPosition, rayParams)


def makeRayBulletTraceRenderer(resolver):
    return RayBulletTraceRenderer(resolver.resolve(RayRenderer))
