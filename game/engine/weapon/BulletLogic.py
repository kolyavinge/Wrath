from game.anx.BulletIdLogic import BulletIdLogic
from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.Random import Random


class BulletLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletIdLogic: BulletIdLogic,
    ):
        self.traversal = traversal
        self.bulletIdLogic = bulletIdLogic

    def makeBullet(self, gameState, person, weapon, id=None, randomSeed=None):
        bullet = weapon.makeBullet(person)
        bullet.id = id or self.bulletIdLogic.getBulletId(person.id)
        if randomSeed is not None:
            bullet.randomSeed = randomSeed
        elif weapon.hasDebrisAfterExplosion:
            bullet.randomSeed = Random.getInt(0, CommonConstants.maxBulletSeed)
        gameState.bullets.append(bullet)
        gameState.bulletsById[bullet.id] = bullet
        bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.collisionTree, bullet.currentPosition)
        bullet.nextLevelSegment = bullet.currentLevelSegment

        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, bullet.currentPosition)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment = visibilityLevelSegment
            visibilityLevelSegment.bullets.append(bullet)

        if visibilityLevelSegment in gameState.visibleLevelSegments:
            flash = weapon.makeFlash()
            if flash is not None:
                visibilityLevelSegment.weaponFlashes.append(flash)

        trace = bullet.makeTrace()
        if trace is not None:
            gameState.bulletTraces.append(trace)
            visibilityLevelSegment.bulletTraces.append(trace)
            trace.visibilityLevelSegments.add(visibilityLevelSegment)

        return bullet

    def removeBullet(self, gameState, removedBullet):
        removedBullet.isAlive = False
        gameState.removedBullets.append(removedBullet)
        gameState.bullets.remove(removedBullet)
        gameState.bulletsById.pop(removedBullet.id)
        if removedBullet.isVisible:
            removedBullet.currentVisibilityLevelSegment.bullets.remove(removedBullet)
