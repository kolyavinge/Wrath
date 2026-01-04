from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.engine.weapon.BulletLogic import BulletLogic


class BulletPositionUpdater:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
        bulletLogic: BulletLogic,
    ):
        self.gameState = gameState
        self.traversal = traversal
        self.bulletLogic = bulletLogic

    def moveNextPosition(self):
        for bullet in self.gameState.bullets:
            self.moveBulletNextPosition(bullet)

    def moveBulletNextPosition(self, bullet):
        if bullet.accelValue > 0:
            bullet.velocityValue += bullet.accelValue
            bullet.velocity.setLength(bullet.velocityValue)
        bullet.totalDistance += bullet.velocityValue
        if bullet.totalDistance < CommonConstants.maxLevelSize:
            bullet.nextPosition.add(bullet.velocity)
            bspTree = self.gameState.collisionTree
            bullet.nextLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.nextPosition)
        else:
            self.bulletLogic.removeBullet(bullet)

    def commitNextPosition(self):
        for bullet in self.gameState.bullets:
            self.commitBulletNextPosition(bullet)

    def commitBulletNextPosition(self, bullet):
        if bullet.isVisible:
            oldVisibilityLevelSegment = bullet.currentVisibilityLevelSegment
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment
            bspTree = self.gameState.visibilityTree
            bullet.currentVisibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            self.moveBulletToNewVisibilityLevelSegment(bullet, oldVisibilityLevelSegment, bullet.currentVisibilityLevelSegment)
        else:
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment

    def moveBulletToNewVisibilityLevelSegment(self, bullet, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.bullets.remove(bullet)
            newLevelSegment.bullets.append(bullet)
