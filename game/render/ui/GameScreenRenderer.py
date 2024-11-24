from game.render.debug.DebugRenderer import DebugRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.NonStandartBulletRenderer import NonStandartBulletRenderer
from game.render.weapon.WeaponFlashRenderer import WeaponFlashRenderer


class GameScreenRenderer:

    def __init__(self, gameScreenInitializer, debugRenderer, mainSceneRenderer, nonStandartBulletRenderer, weaponFlashRenderer, crosshairRenderer):
        self.gameScreenInitializer = gameScreenInitializer
        self.debugRenderer = debugRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.nonStandartBulletRenderer = nonStandartBulletRenderer
        self.weaponFlashRenderer = weaponFlashRenderer
        self.crosshairRenderer = crosshairRenderer

    def init(self):
        self.gameScreenInitializer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()
        self.nonStandartBulletRenderer.render()
        self.weaponFlashRenderer.render()
        self.crosshairRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(
        resolver.resolve(GameScreenInitializer),
        resolver.resolve(DebugRenderer),
        resolver.resolve(MainSceneRenderer),
        resolver.resolve(NonStandartBulletRenderer),
        resolver.resolve(WeaponFlashRenderer),
        resolver.resolve(CrosshairRenderer),
    )
