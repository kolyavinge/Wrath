from game.model.weapon.Plasma import PlasmaRay
from game.render.weapon.PlasmaRayRenderer import PlasmaRayRenderer


class RayRenderer:

    def __init__(
        self,
        plasmaRayRenderer: PlasmaRayRenderer,
    ):
        self.renderers = {}
        self.renderers[PlasmaRay] = plasmaRayRenderer

    def render(self, player, camera, visibleLevelSegments, globalTimeSec):
        visibleRays = self.getVisibleRaysDictionary(visibleLevelSegments)
        if len(visibleRays) == 0:
            return

        for rayType, rays in visibleRays.items():
            self.renderers[rayType].renderRays(rays, player, camera, globalTimeSec)

    def getVisibleRaysDictionary(self, visibleLevelSegments):
        result = {}
        for levelSegment in visibleLevelSegments:
            for ray in levelSegment.rays:
                if type(ray) in result:
                    result[type(ray)].add(ray)
                else:
                    result[type(ray)] = set([ray])

        return result
