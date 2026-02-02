from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class RayLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def makeRay(self, gameState, person, weapon):
        ray = weapon.makeRay(person)
        ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.collisionTree, ray.startPosition)
        ray.endLevelSegment = ray.startLevelSegment
        ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, ray.startPosition)
        ray.visibilityLevelSegment.rays.append(ray)
        ray.initTimeSec = gameState.globalTimeSec
        gameState.rays.append(ray)

        return ray

    def removeRay(self, gameState, ray):
        gameState.rays.remove(ray)
        ray.visibilityLevelSegment.rays.remove(ray)
