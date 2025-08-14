from game.anx.Events import Events
from game.lib.EventManager import EventManager
from game.model.person.AimState import DefaultAimState
from game.render.debug.PlayerSegmentItemsRenderer import PlayerSegmentItemsRenderer
from game.render.level.BackgroundRenderer import BackgroundRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.menu.DashboardRenderer import DashboardRenderer
from game.render.person.PlayerBloodStainRenderer import PlayerBloodStainRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.weapon.BulletTraceRenderer import BulletTraceRenderer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.ShineBulletRenderer import ShineBulletRenderer
from game.render.weapon.SniperCrosshairRenderer import SniperCrosshairRenderer
from game.render.weapon.WeaponFlashRenderer import WeaponFlashRenderer


class GameScreenRenderer:

    def __init__(
        self,
        gameScreenInitializer: GameScreenInitializer,
        backgroundRenderer: BackgroundRenderer,
        mainSceneRenderer: MainSceneRenderer,
        shineBulletRenderer: ShineBulletRenderer,
        weaponFlashRenderer: WeaponFlashRenderer,
        bulletTraceRenderer: BulletTraceRenderer,
        crosshairRenderer: CrosshairRenderer,
        playerBloodStainRenderer: PlayerBloodStainRenderer,
        sniperCrosshairRenderer: SniperCrosshairRenderer,
        dashboardRenderer: DashboardRenderer,
        playerSegmentItemsRenderer: PlayerSegmentItemsRenderer,
        eventManager: EventManager,
    ):
        self.gameScreenInitializer = gameScreenInitializer
        self.backgroundRenderer = backgroundRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.shineBulletRenderer = shineBulletRenderer
        self.weaponFlashRenderer = weaponFlashRenderer
        self.bulletTraceRenderer = bulletTraceRenderer
        self.crosshairRenderer = crosshairRenderer
        self.playerBloodStainRenderer = playerBloodStainRenderer
        self.sniperCrosshairRenderer = sniperCrosshairRenderer
        self.dashboardRenderer = dashboardRenderer
        self.playerSegmentItemsRenderer = playerSegmentItemsRenderer
        self.renderFunc = self.renderDefaultAimState
        eventManager.attachToEvent(Events.aimStateSwitched, self.onAimStateSwitched)

    def init(self):
        self.gameScreenInitializer.init()

    def render(self):
        self.renderFunc()

    def renderDefaultAimState(self):
        self.mainSceneRenderer.renderDefaultAimState()
        # self.playerSegmentItemsRenderer.render()
        self.backgroundRenderer.render()
        self.shineBulletRenderer.render()
        self.weaponFlashRenderer.render()
        self.bulletTraceRenderer.render()
        self.crosshairRenderer.render()
        self.playerBloodStainRenderer.render()
        self.dashboardRenderer.render()

    def renderSniperAimState(self):
        self.mainSceneRenderer.renderSniperAimState()
        self.backgroundRenderer.render()
        self.shineBulletRenderer.render()
        self.weaponFlashRenderer.render()
        self.bulletTraceRenderer.render()
        self.sniperCrosshairRenderer.render()

    def onAimStateSwitched(self, aimState):
        if type(aimState) == DefaultAimState:
            self.renderFunc = self.renderDefaultAimState
        else:
            self.renderFunc = self.renderSniperAimState
