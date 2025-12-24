from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class RayLogic:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def makeRay(self, weapon):
        ray = weapon.makeRay()
        self.gameData.rays.append(ray)
        ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.startPosition)
        ray.endLevelSegment = ray.startLevelSegment
        ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, ray.startPosition)
        ray.visibilityLevelSegment.rays.append(ray)

    def removeRay(self, weapon):
        for ray in self.gameData.rays:
            if ray.weapon == weapon:
                self.gameData.rays.remove(ray)
                return

        assert False
