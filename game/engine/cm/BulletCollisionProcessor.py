from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.GameData import GameData


class BulletCollisionProcessor:

    def __init__(self, gameData, bulletCollisionDetector, traversal):
        self.gameData = gameData
        self.bulletCollisionDetector = bulletCollisionDetector
        self.traversal = traversal

    def process(self):
        for bullet in self.gameData.bullets:
            collisionPoint = self.bulletCollisionDetector.getConstructionCollisionPointOrNone(bullet)
            if collisionPoint is None:
                bullet.commitNextPosition()
                bspTree = self.gameData.level.collisionTree
                bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            else:
                self.gameData.bullets.remove(bullet)


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(resolver.resolve(GameData), resolver.resolve(BulletCollisionDetector), resolver.resolve(BSPTreeTraversal))
