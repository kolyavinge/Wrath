from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.GameData import GameData
from game.model.level.BulletHole import BulletHole


class BulletCollisionProcessor:

    def __init__(self, gameData, bulletCollisionDetector, traversal):
        self.gameData = gameData
        self.bulletCollisionDetector = bulletCollisionDetector
        self.traversal = traversal

    def process(self):
        for bullet in self.gameData.bullets:
            collisionResult = self.bulletCollisionDetector.getConstructionCollisionResultOrNone(bullet)
            if collisionResult is None:
                bullet.commitNextPosition()
                bspTree = self.gameData.level.collisionTree
                bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            else:
                collisionPoint, frontNormal = collisionResult
                bspTree = self.gameData.level.visibilityTree
                visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
                bulletHole = BulletHole()
                bulletHole.position = collisionPoint
                bulletHole.frontNormal = frontNormal
                visibilityLevelSegment.bulletHoles.append(bulletHole)
                self.gameData.bullets.remove(bullet)


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(resolver.resolve(GameData), resolver.resolve(BulletCollisionDetector), resolver.resolve(BSPTreeTraversal))
