from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.lib.Math import Math


class RayPositionUpdater:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
    ):
        self.gameState = gameState
        self.traversal = traversal

    def update(self):
        for ray in self.gameState.rays:
            ray.velocityValue += ray.accelValue
            ray.length = Math.min(ray.length + ray.velocityValue, ray.maxLength)
            ray.startPosition = ray.weapon.barrelPosition
            ray.currentPosition = ray.weapon.direction.copy()
            ray.currentPosition.setLength(ray.length)
            ray.currentPosition.add(ray.startPosition)
            ray.direction = ray.weapon.direction
            ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, ray.startPosition)
            ray.currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, ray.currentPosition)
            oldVisibilityLevelSegment = ray.visibilityLevelSegment
            ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.visibilityTree, ray.startPosition)
            self.moveRayToNewVisibilityLevelSegment(ray, oldVisibilityLevelSegment, ray.visibilityLevelSegment)

    def moveRayToNewVisibilityLevelSegment(self, ray, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.rays.remove(ray)
            newLevelSegment.rays.append(ray)
