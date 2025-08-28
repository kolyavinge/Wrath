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

    def anyCollisions(self, startPoint, endPoint):
        startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, startPoint)
        endLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, endPoint)

        return self.anyWallCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment) or self.anyVoidCollisions(
            startPoint, endPoint, startLevelSegment, endLevelSegment
        )

    def anyWallCollisions(self, startPoint, endPoint, startLevelSegment, endLevelSegment):
        return self.personWallCollisionDetector.anyCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment)

    def anyVoidCollisions(self, startPoint, endPoint, startLevelSegment, endLevelSegment):
        return self.voidCollisionDetector.anyCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment)
