from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class VoidCollisionDetector:

    def __init__(
        self,
        levelSegmentItemFinder: LevelSegmentItemFinder,
    ):
        self.levelSegmentItemFinder = levelSegmentItemFinder

    def anyCollisions(self, startPoint, endPoint, startSegment, endSegment, collisionTree):
        return self.levelSegmentItemFinder.findItemOrNone(
            collisionTree,
            startSegment,
            endSegment,
            startPoint,
            endPoint,
            lambda segment, start, end: self.hasNoFloor(segment),
        )

    def hasNoFloor(self, levelSegment):
        return len(levelSegment.floors) == 0
