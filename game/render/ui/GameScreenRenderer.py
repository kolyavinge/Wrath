from game.anx.Events import Events
from game.lib.EventManager import EventManager
from game.model.AimState import DefaultAimState
from game.render.anx.BackgroundRenderer import BackgroundRenderer
from game.render.debug.DebugRenderer import DebugRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.weapon.BulletTraceRenderer import BulletTraceRenderer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.ShineBulletRenderer import ShineBulletRenderer
from game.render.weapon.SniperCrosshairRenderer import SniperCrosshairRenderer
from game.render.weapon.WeaponFlashRenderer import WeaponFlashRenderer


class GameScreenRenderer:

    def __init__(
        self,
        gameScreenInitializer,
        debugRenderer,
        backgroundRenderer,
        mainSceneRenderer,
        shineBulletRenderer,
        weaponFlashRenderer,
        bulletTraceRenderer,
        crosshairRenderer,
        sniperCrosshairRenderer,
        eventManager,
    ):
        self.gameScreenInitializer = gameScreenInitializer
        self.debugRenderer = debugRenderer
        self.backgroundRenderer = backgroundRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.shineBulletRenderer = shineBulletRenderer
        self.weaponFlashRenderer = weaponFlashRenderer
        self.bulletTraceRenderer = bulletTraceRenderer
        self.crosshairRenderer = crosshairRenderer
        self.sniperCrosshairRenderer = sniperCrosshairRenderer
        self.renderFunc = self.renderDefaultAimState
        eventManager.attachToEvent(Events.aimStateSwitched, self.onAimStateSwitched)

    def init(self):
        self.gameScreenInitializer.init()

    def render(self):
        self.renderFunc()

    def renderDefaultAimState(self):
        self.mainSceneRenderer.render()
        self.backgroundRenderer.render()
        self.shineBulletRenderer.render()
        self.weaponFlashRenderer.render()
        self.bulletTraceRenderer.render()
        self.crosshairRenderer.render()
        # self.debugRenderer.render()

    def renderSniperAimState(self):
        self.mainSceneRenderer.render()
        self.backgroundRenderer.render()
        self.shineBulletRenderer.render()
        self.weaponFlashRenderer.render()
        self.bulletTraceRenderer.render()
        self.sniperCrosshairRenderer.render()

    def onAimStateSwitched(self, aimState):
        if type(aimState) == DefaultAimState:
            self.renderFunc = self.renderDefaultAimState
            self.mainSceneRenderer.renderPlayerWeapon = True
        else:
            self.renderFunc = self.renderSniperAimState
            self.mainSceneRenderer.renderPlayerWeapon = False


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(
        resolver.resolve(GameScreenInitializer),
        resolver.resolve(DebugRenderer),
        resolver.resolve(BackgroundRenderer),
        resolver.resolve(MainSceneRenderer),
        resolver.resolve(ShineBulletRenderer),
        resolver.resolve(WeaponFlashRenderer),
        resolver.resolve(BulletTraceRenderer),
        resolver.resolve(CrosshairRenderer),
        resolver.resolve(SniperCrosshairRenderer),
        resolver.resolve(EventManager),
    )
