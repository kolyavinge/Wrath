from game.anx.CommonConstants import CommonConstants
from game.lib.EventManager import EventManager, Events
from game.model.person.AimState import DefaultAimState
from game.render.anx.VignetteRenderer import VignetteRenderer
from game.render.debug.PlayerSegmentItemsRenderer import PlayerSegmentItemsRenderer
from game.render.level.BackgroundRenderer import BackgroundRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.menu.DashboardRenderer import DashboardRenderer
from game.render.person.EnemyLifeBarRenderer import EnemyLifeBarRenderer
from game.render.person.PlayerBloodStainRenderer import PlayerBloodStainRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.weapon.BulletHoleRenderer import BulletHoleRenderer
from game.render.weapon.BulletTraceRenderer import BulletTraceRenderer
from game.render.weapon.CrosshairRenderer import CrosshairRenderer
from game.render.weapon.ExplosionRenderer import ExplosionRenderer
from game.render.weapon.RayRenderer import RayRenderer
from game.render.weapon.ShineBulletRenderer import ShineBulletRenderer
from game.render.weapon.SniperCrosshairRenderer import SniperCrosshairRenderer
from game.render.weapon.WeaponFlashRenderer import WeaponFlashRenderer
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameScreenRenderer:

    def __init__(
        self,
        gameScreenInitializer: GameScreenInitializer,
        backgroundRenderer: BackgroundRenderer,
        mainSceneRenderer: MainSceneRenderer,
        shineBulletRenderer: ShineBulletRenderer,
        weaponFlashRenderer: WeaponFlashRenderer,
        enemyLifeBarRenderer: EnemyLifeBarRenderer,
        rayRenderer: RayRenderer,
        bulletHoleRenderer: BulletHoleRenderer,
        bulletTraceRenderer: BulletTraceRenderer,
        explosionRenderer: ExplosionRenderer,
        crosshairRenderer: CrosshairRenderer,
        playerBloodStainRenderer: PlayerBloodStainRenderer,
        sniperCrosshairRenderer: SniperCrosshairRenderer,
        vignetteRenderer: VignetteRenderer,
        dashboardRenderer: DashboardRenderer,
        playerSegmentItemsRenderer: PlayerSegmentItemsRenderer,
        eventManager: EventManager,
    ):
        self.gameScreenInitializer = gameScreenInitializer
        self.backgroundRenderer = backgroundRenderer
        self.mainSceneRenderer = mainSceneRenderer
        self.shineBulletRenderer = shineBulletRenderer
        self.weaponFlashRenderer = weaponFlashRenderer
        self.enemyLifeBarRenderer = enemyLifeBarRenderer
        self.rayRenderer = rayRenderer
        self.bulletHoleRenderer = bulletHoleRenderer
        self.bulletTraceRenderer = bulletTraceRenderer
        self.explosionRenderer = explosionRenderer
        self.crosshairRenderer = crosshairRenderer
        self.playerBloodStainRenderer = playerBloodStainRenderer
        self.sniperCrosshairRenderer = sniperCrosshairRenderer
        self.vignetteRenderer = vignetteRenderer
        self.dashboardRenderer = dashboardRenderer
        self.playerSegmentItemsRenderer = playerSegmentItemsRenderer
        self.renderFunc = self.renderDefaultAimState
        eventManager.attachToEvent(Events.aimStateSwitched, self.onAimStateSwitched)

    def init(self, gameState):
        self.gameScreenInitializer.init(gameState)

    # @timeProfile("Rendered", CommonConstants.renderTimerMsec / 1000.0, showOnlyLimited=True)
    # @cpuProfile
    def render(self, gameState):
        self.renderFunc(gameState)

    def renderDefaultAimState(self, gameState):
        self.mainSceneRenderer.renderDefaultAimState()
        # self.playerSegmentItemsRenderer.render(gameState.player, gameState.camera)
        self.backgroundRenderer.render(gameState.backgroundVisibility, gameState.camera)
        self.bulletHoleRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.rayRenderer.render(gameState.player, gameState.camera, gameState.visibleLevelSegments, gameState.globalTimeSec)
        self.shineBulletRenderer.render(gameState.bullets, gameState.player, gameState.camera)
        self.bulletTraceRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.explosionRenderer.render(gameState.visibleLevelSegments, gameState.globalTimeSec)
        self.weaponFlashRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.enemyLifeBarRenderer.render(gameState.enemyLifeBars, gameState.camera)
        self.crosshairRenderer.render()
        self.vignetteRenderer.render()
        self.playerBloodStainRenderer.render(gameState.bloodStains)
        self.dashboardRenderer.render(gameState)

    def renderSniperAimState(self, gameState):
        self.mainSceneRenderer.renderSniperAimState()
        self.backgroundRenderer.render(gameState.backgroundVisibility, gameState.camera)
        self.bulletHoleRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.rayRenderer.render(gameState.player, gameState.camera, gameState.visibleLevelSegments, gameState.globalTimeSec)
        self.shineBulletRenderer.render(gameState.bullets, gameState.player, gameState.camera)
        self.bulletTraceRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.explosionRenderer.render(gameState.visibleLevelSegments, gameState.globalTimeSec)
        self.weaponFlashRenderer.render(gameState.camera, gameState.visibleLevelSegments)
        self.enemyLifeBarRenderer.render(gameState.enemyLifeBars, gameState.camera)
        self.sniperCrosshairRenderer.render()

    def onAimStateSwitched(self, player):
        if type(player.aimState) == DefaultAimState:
            self.renderFunc = self.renderDefaultAimState
        else:
            self.renderFunc = self.renderSniperAimState
