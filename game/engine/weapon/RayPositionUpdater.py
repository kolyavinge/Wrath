from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math


class RayPositionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        for ray in self.gameData.rays:
            ray.length = Math.min(ray.length + ray.velocityValue, ray.maxLength)
            ray.startPosition = ray.weapon.barrelPosition
            ray.currentPosition = ray.weapon.direction.copy()
            ray.currentPosition.setLength(ray.length)
            ray.currentPosition.add(ray.startPosition)
            ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.startPosition)
            ray.currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.currentPosition)
            oldVisibilityLevelSegment = ray.visibilityLevelSegment
            ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, ray.startPosition)
            self.moveRayToNewVisibilityLevelSegment(ray, oldVisibilityLevelSegment, ray.visibilityLevelSegment)

    def moveRayToNewVisibilityLevelSegment(self, ray, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.rays.remove(ray)
            newLevelSegment.rays.append(ray)
