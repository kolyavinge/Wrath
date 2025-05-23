from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.GameData import GameData
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class BulletCollisionTarget:

    construction = 1
    person = 2


class BulletCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        levelSegmentItemFinder: LevelSegmentItemFinder,
        constructionCollisionDetector: ConstructionCollisionDetector,
        personCollisionDetector: PersonCollisionDetector,
    ):
        self.gameData = gameData
        self.levelSegmentItemFinder = levelSegmentItemFinder
        self.constructionCollisionDetector = constructionCollisionDetector
        self.personCollisionDetector = personCollisionDetector

    def getCollisionResultOrNone(self, bullet):
        return self.levelSegmentItemFinder.findItemOrNone(
            self.gameData.collisionTree,
            bullet.currentLevelSegment,
            bullet.nextLevelSegment,
            bullet.currentPosition,
            bullet.nextPosition,
            lambda segment, start, end: self.getTotalCollisionResultOrNone(bullet, segment, start, end),
        )

    def getTotalCollisionResultOrNone(self, bullet, levelSegment, startPoint, endPoint):
        collisionResult = self.personCollisionDetector.getCollisionResultOrNone(bullet.ownerPerson, levelSegment.allPerson, startPoint, endPoint)
        if collisionResult is not None:
            return (BulletCollisionTarget.person, collisionResult)

        collisionResult = self.constructionCollisionDetector.getCollisionResultOrNone(levelSegment.allConstructions, startPoint, endPoint)
        if collisionResult is not None:
            return (BulletCollisionTarget.construction, collisionResult)

        return None
