from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class BulletMoveLogic:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def process(self):
        for bullet in self.gameData.bullets:
            self.moveBullet(bullet)

    def moveBullet(self, bullet):
        bullet.totalDistance += bullet.velocityValue
        if bullet.totalDistance < CommonConstants.maxLevelSize:
            bullet.nextPosition.add(bullet.velocity)
            bspTree = self.gameData.level.collisionTree
            bullet.nextLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.nextPosition)
        else:
            self.gameData.bullets.remove(bullet)


def makeBulletMoveLogic(resolver):
    return BulletMoveLogic(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
