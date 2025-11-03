from game.engine.GameData import GameData
from game.model.weapon.Launcher import LauncherExplosion
from game.model.weapon.Plasma import PlasmaExplosion
from game.render.weapon.explosion.LauncherExplosionRenderer import *
from game.render.weapon.explosion.PlasmaExplosionRenderer import PlasmaExplosionRenderer


class ExplosionRenderer:

    def __init__(
        self,
        gameData: GameData,
        plasmaExplosionRenderer: PlasmaExplosionRenderer,
        launcherExplosionRenderer: LauncherExplosionRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[PlasmaExplosion] = plasmaExplosionRenderer
        self.renderers[LauncherExplosion] = launcherExplosionRenderer

    def render(self):
        visibleExplosions = self.getVisibleExplosionsDictionary()
        if len(visibleExplosions) == 0:
            return

        for explosionType, explosions in visibleExplosions.items():
            self.renderers[explosionType].renderExplosions(explosions)

    def getVisibleExplosionsDictionary(self):
        result = {}
        for levelSegment in self.gameData.visibleLevelSegments:
            for explosion in levelSegment.explosions:
                if type(explosion) in result:
                    result[type(explosion)].add(explosion)
                else:
                    result[type(explosion)] = set([explosion])

        return result
