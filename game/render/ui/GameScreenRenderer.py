from game.render.debug.DebugRenderer import DebugRenderer
from game.render.level.LevelRenderer import LevelRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.weapon.PlayerWeaponRenderer import PlayerWeaponRenderer


class GameScreenRenderer:

    def __init__(self, debugRenderer, levelRenderer, playerWeaponRenderer, mainSceneRenderer):
        self.debugRenderer = debugRenderer
        self.levelRenderer = levelRenderer
        self.playerWeaponRenderer = playerWeaponRenderer
        self.mainSceneRenderer = mainSceneRenderer

    def init(self):
        self.levelRenderer.init()
        self.playerWeaponRenderer.init()
        # self.mainSceneRenderer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(
        resolver.resolve(DebugRenderer), resolver.resolve(LevelRenderer), resolver.resolve(PlayerWeaponRenderer), resolver.resolve(MainSceneRenderer)
    )
