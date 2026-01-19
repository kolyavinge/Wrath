from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class RayCollisionDetector:

    def __init__(
        self,
        levelSegmentItemFinder: LevelSegmentItemFinder,
        constructionCollisionDetector: ConstructionCollisionDetector,
        personCollisionDetector: PersonCollisionDetector,
    ):
        self.levelSegmentItemFinder = levelSegmentItemFinder
        self.constructionCollisionDetector = constructionCollisionDetector
        self.personCollisionDetector = personCollisionDetector

    def getCollisionResultOrNone(self, ray, collisionTree):
        return self.levelSegmentItemFinder.findItemOrNone(
            collisionTree,
            ray.startLevelSegment,
            ray.currentLevelSegment,
            ray.startPosition,
            ray.currentPosition,
            lambda segment, start, end: self.getTotalCollisionResultOrNone(ray, segment, start, end),
        )

    def getTotalCollisionResultOrNone(self, ray, levelSegment, startPoint, endPoint):
        # check person
        collisionResult = self.personCollisionDetector.getNearestCollisionResultOrNone(ray.ownerPerson, levelSegment.allPerson, startPoint, endPoint)
        if collisionResult is not None:
            return (CollidedTarget.onePerson, collisionResult)

        # check constructions
        collisionResult = self.constructionCollisionDetector.getCollisionResultOrNone(levelSegment.allConstructions, startPoint, endPoint)
        if collisionResult is not None:
            return (CollidedTarget.construction, collisionResult)

        return None
