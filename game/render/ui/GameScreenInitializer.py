from game.engine.GameData import GameData
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class GameScreenInitializer:

    def __init__(
        self,
        gameData,
        levelItemRenderCollection,
        bulletHoleRenderCollection,
        shadowCasterRenderCollection,
        weaponRenderCollection,
        weaponFlashRenderCollection,
    ):
        self.gameData = gameData
        self.levelItemRenderCollection = levelItemRenderCollection
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.weaponFlashRenderCollection = weaponFlashRenderCollection

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelItemRenderCollection.init(allLevelSegments)
        self.bulletHoleRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
        self.weaponRenderCollection.init()
        self.weaponFlashRenderCollection.init()


def makeGameScreenInitializer(resolver):
    return GameScreenInitializer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemRenderCollection),
        resolver.resolve(BulletHoleRenderCollection),
        resolver.resolve(ShadowCasterRenderCollection),
        resolver.resolve(WeaponRenderCollection),
        resolver.resolve(WeaponFlashRenderCollection),
    )
