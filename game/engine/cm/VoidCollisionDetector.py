from game.engine.GameData import GameData
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class VoidCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        levelSegmentItemFinder: LevelSegmentItemFinder,
    ):
        self.gameData = gameData
        self.levelSegmentItemFinder = levelSegmentItemFinder

    def anyCollisions(self, startPoint, endPoint, startSegment, endSegment):
        return self.levelSegmentItemFinder.findItemOrNone(
            self.gameData.collisionTree,
            startSegment,
            endSegment,
            startPoint,
            endPoint,
            lambda segment, start, end: self.hasNoFloor(segment),
        )

    def hasNoFloor(self, levelSegment):
        return len(levelSegment.floors) == 0
