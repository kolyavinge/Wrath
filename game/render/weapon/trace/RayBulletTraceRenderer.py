from game.render.anx.RayRenderer import RayRenderer


class RayBulletTraceRenderer:

    def __init__(self, rayRenderer: RayRenderer):
        self.rayRenderer = rayRenderer

    def renderTraces(self, traces, rayParams):
        self.rayRenderer.render(traces, rayParams)
