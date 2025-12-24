from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class RayUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        for ray in self.gameData.rays:
            ray.update()
            ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.startPosition)
            ray.endLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.endPosition)
            oldVisibilityLevelSegment = ray.visibilityLevelSegment
            ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, ray.startPosition)
            self.moveRayToNewVisibilityLevelSegment(ray, oldVisibilityLevelSegment, ray.visibilityLevelSegment)

    def moveRayToNewVisibilityLevelSegment(self, ray, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.rays.remove(ray)
            newLevelSegment.rays.append(ray)
