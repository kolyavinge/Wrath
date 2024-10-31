from game.render.debug.DebugRenderer import DebugRenderer
from game.render.level.LevelRenderer import LevelRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.PlayerWeaponRenderer import PlayerWeaponRenderer


class GameScreenRenderer:

    def __init__(self, debugRenderer, levelRenderer, playerWeaponRenderer, mainSceneRenderer, crosshairRenderer):
        self.debugRenderer = debugRenderer
        self.levelRenderer = levelRenderer
        self.playerWeaponRenderer = playerWeaponRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.crosshairRenderer = crosshairRenderer

    def init(self):
        self.levelRenderer.init()
        self.playerWeaponRenderer.init()
        self.mainSceneRenderer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()
        self.crosshairRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(
        resolver.resolve(DebugRenderer),
        resolver.resolve(LevelRenderer),
        resolver.resolve(PlayerWeaponRenderer),
        resolver.resolve(MainSceneRenderer),
        resolver.resolve(CrosshairRenderer),
    )
