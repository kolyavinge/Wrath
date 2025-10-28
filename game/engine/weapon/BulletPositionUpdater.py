from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.weapon.BulletLogic import BulletLogic


class BulletPositionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        bulletLogic: BulletLogic,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.bulletLogic = bulletLogic

    def moveNextPosition(self):
        for bullet in self.gameData.bullets:
            self.moveBulletNextPosition(bullet)

    def moveBulletNextPosition(self, bullet):
        bullet.totalDistance += bullet.velocityValue
        if bullet.totalDistance < CommonConstants.maxLevelSize:
            bullet.nextPosition.add(bullet.velocity)
            bspTree = self.gameData.collisionTree
            bullet.nextLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.nextPosition)
        else:
            self.bulletLogic.removeBullet(bullet)

    def commitNextPosition(self):
        for bullet in self.gameData.bullets:
            self.commitBulletNextPosition(bullet)

    def commitBulletNextPosition(self, bullet):
        if bullet.isVisible:
            oldVisibilityLevelSegment = bullet.currentVisibilityLevelSegment
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment
            bspTree = self.gameData.visibilityTree
            bullet.currentVisibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            self.moveBulletToNewVisibilityLevelSegment(bullet, oldVisibilityLevelSegment, bullet.currentVisibilityLevelSegment)
        else:
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment

    def moveBulletToNewVisibilityLevelSegment(self, bullet, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.bullets.remove(bullet)
            newLevelSegment.bullets.append(bullet)
