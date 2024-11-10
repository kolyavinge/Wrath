from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.GameData import GameData
from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class BulletCollisionDetector:

    def __init__(self, gameData, levelSegmentItemFinder, constructionCollisionDetector):
        self.gameData = gameData
        self.levelSegmentItemFinder = levelSegmentItemFinder
        self.constructionCollisionDetector = constructionCollisionDetector

    def getConstructionCollisionResultOrNone(self, bullet):
        return self.levelSegmentItemFinder.findItemOrNone(
            self.gameData.level.collisionTree,
            bullet.currentLevelSegment,
            bullet.nextLevelSegment,
            bullet.currentPosition,
            bullet.nextPosition,
            self.constructionCollisionDetector.getCollisionResultOrNone,
        )


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector(
        resolver.resolve(GameData), resolver.resolve(LevelSegmentItemFinder), resolver.resolve(ConstructionCollisionDetector)
    )
