from game.anx.BulletIdLogic import BulletIdLogic
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class BulletLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletIdLogic: BulletIdLogic,
    ):
        self.traversal = traversal
        self.bulletIdLogic = bulletIdLogic

    def makeBullet(self, gameState, person, weapon, id=None):
        bullet = weapon.makeBullet(person)
        bullet.id = id or self.bulletIdLogic.getNextBulletId(person.id)
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

    def makeDebris(self, gameState, explosion):
        debris = explosion.makeDebris()
        if debris is None:
            return

        currentLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.collisionTree, explosion.position)
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, explosion.position)

        for piece in debris:
            gameState.bullets.append(piece)
            piece.currentLevelSegment = currentLevelSegment
            piece.nextLevelSegment = currentLevelSegment

            if piece.isVisible:
                piece.currentVisibilityLevelSegment = visibilityLevelSegment
                visibilityLevelSegment.bullets.append(piece)

            trace = piece.makeTrace()
            if trace is not None:
                gameState.bulletTraces.append(trace)
                visibilityLevelSegment.bulletTraces.append(trace)
                trace.visibilityLevelSegments.add(visibilityLevelSegment)

    def removeBullet(self, gameState, bullet):
        bullet.isAlive = False
        gameState.bulletsToRemove.append(bullet)
