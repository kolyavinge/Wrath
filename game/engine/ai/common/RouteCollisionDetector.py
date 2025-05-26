from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.WallCollisionDetector import WallCollisionDetector
from game.engine.GameData import GameData


class RouteCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        wallCollisionDetector: WallCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.wallCollisionDetector = wallCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, pointFrom, pointTo):
        pointFromLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointFrom)
        pointToLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, pointTo)

        return self.anyWallCollisions(pointFrom, pointTo, pointFromLevelSegment, pointToLevelSegment) or self.anyVoidCollisions(pointToLevelSegment)

    def anyWallCollisions(self, pointFrom, pointTo, pointFromLevelSegment, pointToLevelSegment):
        for wall in pointFromLevelSegment.walls:
            if self.wallCollisionDetector.lineIntersectsWall(pointFrom, pointTo, wall):
                return True

        if pointFromLevelSegment != pointToLevelSegment:
            for wall in pointToLevelSegment.walls:
                if self.wallCollisionDetector.lineIntersectsWall(pointFrom, pointTo, wall):
                    return True

        return False

    def anyVoidCollisions(self, pointToLevelSegment):
        return len(pointToLevelSegment.floors) == 0
