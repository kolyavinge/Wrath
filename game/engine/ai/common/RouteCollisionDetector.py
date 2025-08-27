from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.PersonWallCollisionDetector import PersonWallCollisionDetector
from game.engine.cm.VoidCollisionDetector import VoidCollisionDetector
from game.engine.GameData import GameData


class RouteCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        personWallCollisionDetector: PersonWallCollisionDetector,
        voidCollisionDetector: VoidCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.personWallCollisionDetector = personWallCollisionDetector
        self.voidCollisionDetector = voidCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, pointFrom, pointTo):
        fromLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointFrom)
        toLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointTo)

        return self.anyWallCollisions(pointFrom, pointTo, fromLevelSegment, toLevelSegment) or self.anyVoidCollisions(
            pointFrom, pointTo, fromLevelSegment, toLevelSegment
        )

    def anyWallCollisions(self, pointFrom, pointTo, fromLevelSegment, toLevelSegment):
        return self.personWallCollisionDetector.anyCollisions(pointFrom, pointTo, fromLevelSegment, toLevelSegment)

    def anyVoidCollisions(self, pointFrom, pointTo, fromLevelSegment, toLevelSegment):
        return self.voidCollisionDetector.anyCollisions(pointFrom, pointTo, fromLevelSegment, toLevelSegment)
