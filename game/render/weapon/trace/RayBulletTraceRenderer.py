from game.render.anx.PlaneRayRenderer import PlaneRayRenderer


class RayBulletTraceRenderer:

    def __init__(self, planeRayRenderer: PlaneRayRenderer):
        self.planeRayRenderer = planeRayRenderer

    def renderTraces(self, traces, rayParams, camera):
        self.planeRayRenderer.render(traces, rayParams, camera)
