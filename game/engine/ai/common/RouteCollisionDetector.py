from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.PersonWallCollisionDetector import PersonWallCollisionDetector
from game.engine.cm.VoidCollisionDetector import VoidCollisionDetector


class RouteCollisionDetector:

    def __init__(
        self,
        personWallCollisionDetector: PersonWallCollisionDetector,
        voidCollisionDetector: VoidCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.personWallCollisionDetector = personWallCollisionDetector
        self.voidCollisionDetector = voidCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, startPoint, endPoint, collisionTree):
        startLevelSegment = self.traversal.findLevelSegment(collisionTree, startPoint)
        endLevelSegment = self.traversal.findLevelSegment(collisionTree, endPoint)

        return self.anyWallCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree) or self.anyVoidCollisions(
            startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree
        )

    def anyWallCollisions(self, startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree):
        return self.personWallCollisionDetector.anyCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree)

    def anyVoidCollisions(self, startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree):
        return self.voidCollisionDetector.anyCollisions(startPoint, endPoint, startLevelSegment, endLevelSegment, collisionTree)
