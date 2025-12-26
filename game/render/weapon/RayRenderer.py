from game.engine.GameData import GameData
from game.model.weapon.Plasma import PlasmaRay
from game.render.weapon.PlasmaRayRenderer import PlasmaRayRenderer


class RayRenderer:

    def __init__(
        self,
        gameData: GameData,
        plasmaRayRenderer: PlasmaRayRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[PlasmaRay] = plasmaRayRenderer

    def render(self):
        visibleRays = self.getVisibleRaysDictionary()
        if len(visibleRays) == 0:
            return

        for rayType, rays in visibleRays.items():
            self.renderers[rayType].renderRays(rays)

    def getVisibleRaysDictionary(self):
        result = {}
        for levelSegment in self.gameData.visibleLevelSegments:
            for ray in levelSegment.rays:
                if type(ray) in result:
                    result[type(ray)].add(ray)
                else:
                    result[type(ray)] = set([ray])

        return result
