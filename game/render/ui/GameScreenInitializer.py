from game.render.level.BackgroundRenderer import BackgroundRenderer
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.menu.DashboardRenderer import DashboardRenderer
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection
from game.render.person.PlayerBloodStainRenderCollection import *
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection
from game.render.weapon.BulletRenderCollection import BulletRenderCollection
from game.render.weapon.explosion.FireExplosionRenderer import FireExplosionRenderer
from game.render.weapon.explosion.PlasmaExplosionRenderer import PlasmaExplosionRenderer
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection
from game.tools.timeProfile import timeProfile


class GameScreenInitializer:

    def __init__(
        self,
        levelItemRenderCollection: LevelItemRenderCollection,
        bulletHoleRenderCollection: BulletHoleRenderCollection,
        shadowCasterRenderCollection: ShadowCasterRenderCollection,
        bulletRenderCollection: BulletRenderCollection,
        backgroundRenderer: BackgroundRenderer,
        weaponRenderCollection: WeaponRenderCollection,
        powerupRenderCollection: PowerupRenderCollection,
        weaponFlashRenderCollection: WeaponFlashRenderCollection,
        fireExplosionRenderer: FireExplosionRenderer,
        plasmaExplosionRenderer: PlasmaExplosionRenderer,
        playerBloodStainRenderCollection: PlayerBloodStainRenderCollection,
        enemyRenderCollection: EnemyRenderCollection,
        enemyAnimationCollection: EnemyAnimationCollection,
        dashboardRenderer: DashboardRenderer,
        mainSceneRenderer: MainSceneRenderer,
    ):
        self.levelItemRenderCollection = levelItemRenderCollection
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.bulletRenderCollection = bulletRenderCollection
        self.backgroundRenderer = backgroundRenderer
        self.weaponRenderCollection = weaponRenderCollection
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponFlashRenderCollection = weaponFlashRenderCollection
        self.fireExplosionRenderer = fireExplosionRenderer
        self.plasmaExplosionRenderer = plasmaExplosionRenderer
        self.playerBloodStainRenderCollection = playerBloodStainRenderCollection
        self.enemyRenderCollection = enemyRenderCollection
        self.enemyAnimationCollection = enemyAnimationCollection
        self.dashboardRenderer = dashboardRenderer
        self.mainSceneRenderer = mainSceneRenderer

    # @timeProfile("GameScreenInitializer")
    def init(self, gameState):
        allVisibilityLevelSegments = gameState.visibilityTree.allLevelSegments
        self.levelItemRenderCollection.init(allVisibilityLevelSegments)
        # self.levelItemRenderCollection.init(allVisibilityLevelSegments + self.gameState.collisionTree.allLevelSegments)
        self.bulletHoleRenderCollection.init(allVisibilityLevelSegments)
        self.shadowCasterRenderCollection.init(allVisibilityLevelSegments)
        self.backgroundRenderer.init(gameState.backgroundVisibility)
        self.bulletRenderCollection.init()
        self.weaponRenderCollection.init()
        self.powerupRenderCollection.init()
        self.weaponFlashRenderCollection.init()
        self.fireExplosionRenderer.init(gameState.camera)
        self.plasmaExplosionRenderer.init(gameState.camera)
        self.playerBloodStainRenderCollection.init()
        self.enemyRenderCollection.init()
        self.dashboardRenderer.init(gameState.dashboard)
        self.mainSceneRenderer.init(gameState)
