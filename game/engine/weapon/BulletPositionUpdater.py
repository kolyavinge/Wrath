from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class BulletPositionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

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
            self.gameData.bullets.remove(bullet)
            if bullet.isVisible:
                bullet.currentVisibilityLevelSegment.bullets.remove(bullet)

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
