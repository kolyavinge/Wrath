from game.engine.GameData import GameData
from game.lib.Stopwatch import Stopwatch
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection
from game.render.weapon.BulletRenderCollection import BulletRenderCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


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
        enemyRenderCollection: EnemyRenderCollection,
    ):
        self.gameData = gameData
        self.levelItemRenderCollection = levelItemRenderCollection
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.bulletRenderCollection = bulletRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponFlashRenderCollection = weaponFlashRenderCollection
        self.enemyRenderCollection = enemyRenderCollection

    def init(self):
        allLevelSegments = self.gameData.visibilityTree.getAllLevelSegments()

        sw = Stopwatch()
        sw.start()

        self.levelItemRenderCollection.init(allLevelSegments)
        self.bulletHoleRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
        self.bulletRenderCollection.init()
        self.weaponRenderCollection.init()
        self.powerupRenderCollection.init()
        self.weaponFlashRenderCollection.init()
        self.enemyRenderCollection.init()

        sw.stop()
        print(f"GameScreenInitializer: {sw.elapsed:.8f}")
