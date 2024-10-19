from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.BulletHoleFactory import BulletHoleFactory
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.GameData import GameData


class BulletCollisionProcessor:

    def __init__(self, gameData, traversal, bulletCollisionDetector, bulletHoleFactory):
        self.gameData = gameData
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleFactory = bulletHoleFactory

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
                bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal)
                visibilityLevelSegment.bulletHoles.append(bulletHole)
                self.gameData.bullets.remove(bullet)


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(
        resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal), resolver.resolve(BulletCollisionDetector), resolver.resolve(BulletHoleFactory)
    )
