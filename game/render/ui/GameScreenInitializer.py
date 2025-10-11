from game.engine.GameData import GameData
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.menu.DashboardRenderer import DashboardRenderer
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection
from game.render.person.PlayerBloodStainRenderCollection import *
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection
from game.render.weapon.BulletRenderCollection import BulletRenderCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection
from game.tools.timeProfile import timeProfile


class GameScreenInitializer:

    def __init__(
        self,
        gameData: GameData,
        levelItemRenderCollection: LevelItemRenderCollection,
        bulletHoleRenderCollection: BulletHoleRenderCollection,
        shadowCasterRenderCollection: ShadowCasterRenderCollection,
        bulletRenderCollection: BulletRenderCollection,
        weaponRenderCollection: WeaponRenderCollection,
        powerupRenderCollection: PowerupRenderCollection,
        weaponFlashRenderCollection: WeaponFlashRenderCollection,
        playerBloodStainRenderCollection: PlayerBloodStainRenderCollection,
        enemyRenderCollection: EnemyRenderCollection,
        enemyAnimationCollection: EnemyAnimationCollection,
        dashboardRenderer: DashboardRenderer,
    ):
        self.gameData = gameData
        self.levelItemRenderCollection = levelItemRenderCollection
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.bulletRenderCollection = bulletRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponFlashRenderCollection = weaponFlashRenderCollection
        self.playerBloodStainRenderCollection = playerBloodStainRenderCollection
        self.enemyRenderCollection = enemyRenderCollection
        self.enemyAnimationCollection = enemyAnimationCollection
        self.dashboardRenderer = dashboardRenderer

    # @timeProfile("GameScreenInitializer")
    def init(self):
        allVisibilityLevelSegments = self.gameData.visibilityTree.getAllLevelSegments()
        self.levelItemRenderCollection.init(allVisibilityLevelSegments)
        # self.levelItemRenderCollection.init(allVisibilityLevelSegments + self.gameData.collisionTree.getAllLevelSegments())
        self.bulletHoleRenderCollection.init(allVisibilityLevelSegments)
        self.shadowCasterRenderCollection.init(allVisibilityLevelSegments)
        self.bulletRenderCollection.init()
        self.weaponRenderCollection.init()
        self.powerupRenderCollection.init()
        self.weaponFlashRenderCollection.init()
        self.playerBloodStainRenderCollection.init()
        self.enemyRenderCollection.init()
        self.enemyAnimationCollection.init()
        self.dashboardRenderer.init()
