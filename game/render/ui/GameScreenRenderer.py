from game.render.debug.DebugRenderer import DebugRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.WeaponFlashRenderer import WeaponFlashRenderer


class GameScreenRenderer:

    def __init__(self, gameScreenInitializer, debugRenderer, mainSceneRenderer, crosshairRenderer, weaponFlashRenderer):
        self.gameScreenInitializer = gameScreenInitializer
        self.debugRenderer = debugRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.crosshairRenderer = crosshairRenderer
        self.weaponFlashRenderer = weaponFlashRenderer

    def init(self):
        self.gameScreenInitializer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()
        self.crosshairRenderer.render()
        self.weaponFlashRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(
        resolver.resolve(GameScreenInitializer),
        resolver.resolve(DebugRenderer),
        resolver.resolve(MainSceneRenderer),
        resolver.resolve(CrosshairRenderer),
        resolver.resolve(WeaponFlashRenderer),
    )
