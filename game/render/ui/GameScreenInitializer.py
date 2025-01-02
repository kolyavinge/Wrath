import time

from game.engine.GameData import GameData
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection
from game.render.weapon.BulletRenderCollection import BulletRenderCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class GameScreenInitializer:

    def __init__(
        self,
        gameData,
        levelItemRenderCollection,
        bulletHoleRenderCollection,
        shadowCasterRenderCollection,
        bulletRenderCollection,
        weaponRenderCollection,
        powerupRenderCollection,
        weaponFlashRenderCollection,
    ):
        self.gameData = gameData
        self.levelItemRenderCollection = levelItemRenderCollection
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.bulletRenderCollection = bulletRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponFlashRenderCollection = weaponFlashRenderCollection

    def init(self):
        allLevelSegments = self.gameData.visibilityTree.getAllLevelSegments()

        start = time.time()

        self.levelItemRenderCollection.init(allLevelSegments)
        self.bulletHoleRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
        self.bulletRenderCollection.init()
        self.weaponRenderCollection.init()
        self.powerupRenderCollection.init()
        self.weaponFlashRenderCollection.init()

        end = time.time()
        print(f"GameScreenInitializer: {end-start:.8f}")


def makeGameScreenInitializer(resolver):
    return GameScreenInitializer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemRenderCollection),
        resolver.resolve(BulletHoleRenderCollection),
        resolver.resolve(ShadowCasterRenderCollection),
        resolver.resolve(BulletRenderCollection),
        resolver.resolve(WeaponRenderCollection),
        resolver.resolve(PowerupRenderCollection),
        resolver.resolve(WeaponFlashRenderCollection),
    )
