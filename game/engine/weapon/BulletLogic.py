from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class BulletLogic:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def makeBullet(self, person, weapon):
        bullet = weapon.makeBullet(person)
        self.gameData.bullets.append(bullet)
        bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, bullet.currentPosition)
        bullet.nextLevelSegment = bullet.currentLevelSegment

        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, bullet.currentPosition)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment = visibilityLevelSegment
            visibilityLevelSegment.bullets.append(bullet)

        if visibilityLevelSegment in self.gameData.visibleLevelSegments:
            flash = weapon.makeFlash()
            if flash is not None:
                visibilityLevelSegment.weaponFlashes.append(flash)

        trace = bullet.makeTrace()
        if trace is not None:
            self.gameData.bulletTraces.append(trace)
            visibilityLevelSegment.bulletTraces.append(trace)
            trace.visibilityLevelSegments.add(visibilityLevelSegment)
