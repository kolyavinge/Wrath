from game.engine.GameData import GameData
from game.engine.PlasmaBulletMovingLogic import PlasmaBulletMovingLogic
from game.model.weapon.Plasma import PlasmaBullet


class NonStandardBulletMovingLogic:

    def __init__(self, gameData, plasmaBulletMovingLogic):
        self.gameData = gameData
        self.bulletMovingLogic = {}
        self.bulletMovingLogic[PlasmaBullet] = plasmaBulletMovingLogic

    def apply(self):
        for bullet in self.gameData.bullets:
            bulletType = type(bullet)
            if bulletType in self.bulletMovingLogic:
                self.bulletMovingLogic[bulletType].apply(bullet)


def makeNonStandardBulletMovingLogic(resolver):
    return NonStandardBulletMovingLogic(resolver.resolve(GameData), resolver.resolve(PlasmaBulletMovingLogic))
