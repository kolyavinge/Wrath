from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState


class BulletLogic:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
    ):
        self.gameState = gameState
        self.traversal = traversal

    def makeBullet(self, person, weapon):
        bullet = weapon.makeBullet(person)
        self.gameState.bullets.append(bullet)
        bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, bullet.currentPosition)
        bullet.nextLevelSegment = bullet.currentLevelSegment

        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.visibilityTree, bullet.currentPosition)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment = visibilityLevelSegment
            visibilityLevelSegment.bullets.append(bullet)

        if visibilityLevelSegment in self.gameState.visibleLevelSegments:
            flash = weapon.makeFlash()
            if flash is not None:
                visibilityLevelSegment.weaponFlashes.append(flash)

        trace = bullet.makeTrace()
        if trace is not None:
            self.gameState.bulletTraces.append(trace)
            visibilityLevelSegment.bulletTraces.append(trace)
            trace.visibilityLevelSegments.add(visibilityLevelSegment)

    def makeDebris(self, explosion):
        debris = explosion.makeDebris()
        if debris is None:
            return

        currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, explosion.position)
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.visibilityTree, explosion.position)

        for piece in debris:
            self.gameState.bullets.append(piece)
            piece.currentLevelSegment = currentLevelSegment
            piece.nextLevelSegment = currentLevelSegment

            if piece.isVisible:
                piece.currentVisibilityLevelSegment = visibilityLevelSegment
                visibilityLevelSegment.bullets.append(piece)

            trace = piece.makeTrace()
            if trace is not None:
                self.gameState.bulletTraces.append(trace)
                visibilityLevelSegment.bulletTraces.append(trace)
                trace.visibilityLevelSegments.add(visibilityLevelSegment)

    def removeBullet(self, bullet):
        bullet.isAlive = False
        self.gameState.bulletsToRemove.append(bullet)
