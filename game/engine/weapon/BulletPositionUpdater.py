from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.weapon.BulletLogic import BulletLogic


class BulletPositionUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletLogic: BulletLogic,
    ):
        self.traversal = traversal
        self.bulletLogic = bulletLogic

    def moveNextPosition(self, gameState):
        for bullet in gameState.bullets:
            self.moveBulletNextPosition(gameState, bullet)

    def moveBulletNextPosition(self, gameState, bullet):
        if bullet.accelValue > 0:
            bullet.velocityValue += bullet.accelValue
            bullet.velocity.setLength(bullet.velocityValue)
        bullet.totalDistance += bullet.velocityValue
        if bullet.totalDistance < CommonConstants.maxLevelSize:
            bullet.nextPosition.add(bullet.velocity)
            bspTree = gameState.collisionTree
            bullet.nextLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.nextPosition)
        else:
            self.bulletLogic.removeBullet(bullet)

    def commitNextPosition(self, gameState):
        visibilityTree = gameState.visibilityTree
        for bullet in gameState.bullets:
            self.commitBulletNextPosition(bullet, visibilityTree)

    def commitBulletNextPosition(self, bullet, visibilityTree):
        if bullet.isVisible:
            oldVisibilityLevelSegment = bullet.currentVisibilityLevelSegment
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment
            bullet.currentVisibilityLevelSegment = self.traversal.findLevelSegmentOrNone(visibilityTree, bullet.currentPosition)
            self.moveBulletToNewVisibilityLevelSegment(bullet, oldVisibilityLevelSegment, bullet.currentVisibilityLevelSegment)
        else:
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment

    def moveBulletToNewVisibilityLevelSegment(self, bullet, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.bullets.remove(bullet)
            newLevelSegment.bullets.append(bullet)
