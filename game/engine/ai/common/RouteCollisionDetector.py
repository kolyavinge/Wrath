from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.VoidCollisionDetector import VoidCollisionDetector
from game.engine.cm.WallCollisionDetector import WallCollisionDetector
from game.engine.GameData import GameData


class RouteCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        wallCollisionDetector: WallCollisionDetector,
        voidCollisionDetector: VoidCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.wallCollisionDetector = wallCollisionDetector
        self.voidCollisionDetector = voidCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, pointFrom, pointTo):
        fromLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointFrom)
        toLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointTo)

        return self.anyWallCollisions(pointFrom, pointTo, fromLevelSegment, toLevelSegment) or self.anyVoidCollisions(
            pointFrom, pointTo, fromLevelSegment, toLevelSegment
        )

    def anyWallCollisions(self, pointFrom, pointTo, fromLevelSegment, toLevelSegment):
        result = self.wallCollisionDetector.getCollisionResultOrNone(pointFrom, pointTo, fromLevelSegment, toLevelSegment)
        return result is not None

    def anyVoidCollisions(self, pointFrom, pointTo, fromLevelSegment, toLevelSegment):
        return self.voidCollisionDetector.hasCollisions(pointFrom, pointTo, fromLevelSegment, toLevelSegment)
