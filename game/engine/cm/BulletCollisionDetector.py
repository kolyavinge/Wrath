from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.GameState import GameState
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class BulletCollisionDetector:

    def __init__(
        self,
        gameData: GameState,
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
        # check person
        ownerPerson = bullet.ownerPerson
        allPerson = levelSegment.allPerson
        if bullet.goThroughPerson:
            collisionResult = self.personCollisionDetector.getAllCollisionResultOrNone(ownerPerson, allPerson, startPoint, endPoint)
            if collisionResult is not None:
                return (CollidedTarget.allPerson, collisionResult)
        else:
            collisionResult = self.personCollisionDetector.getNearestCollisionResultOrNone(ownerPerson, allPerson, startPoint, endPoint)
            if collisionResult is not None:
                return (CollidedTarget.onePerson, collisionResult)

        # check constructions
        collisionResult = self.constructionCollisionDetector.getCollisionResultOrNone(levelSegment.allConstructions, startPoint, endPoint)
        if collisionResult is not None:
            return (CollidedTarget.construction, collisionResult)

        return None
