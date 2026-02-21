from game.anx.BulletIdLogic import BulletIdLogic
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class RayLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletIdLogic: BulletIdLogic,
    ):
        self.traversal = traversal
        self.bulletIdLogic = bulletIdLogic

    def makeRay(self, gameState, person, weapon, id=None):
        ray = weapon.makeRay(person)
        ray.id = id or self.bulletIdLogic.getBulletId(person.id)
        ray.startLevelSegment = self.traversal.findLevelSegment(gameState.collisionTree, ray.startPosition)
        ray.endLevelSegment = ray.startLevelSegment
        ray.visibilityLevelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, ray.startPosition)
        ray.visibilityLevelSegment.rays.append(ray)
        ray.initTimeSec = gameState.globalTimeSec
        gameState.rays.append(ray)

        return ray

    def removeRay(self, gameState, ray):
        gameState.rays.remove(ray)
        ray.visibilityLevelSegment.rays.remove(ray)
