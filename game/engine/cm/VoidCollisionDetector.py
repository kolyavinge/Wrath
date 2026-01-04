from game.engine.GameState import GameState
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class VoidCollisionDetector:

    def __init__(
        self,
        gameState: GameState,
        levelSegmentItemFinder: LevelSegmentItemFinder,
    ):
        self.gameState = gameState
        self.levelSegmentItemFinder = levelSegmentItemFinder

    def anyCollisions(self, startPoint, endPoint, startSegment, endSegment):
        return self.levelSegmentItemFinder.findItemOrNone(
            self.gameState.collisionTree,
            startSegment,
            endSegment,
            startPoint,
            endPoint,
            lambda segment, start, end: self.hasNoFloor(segment),
        )

    def hasNoFloor(self, levelSegment):
        return len(levelSegment.floors) == 0
