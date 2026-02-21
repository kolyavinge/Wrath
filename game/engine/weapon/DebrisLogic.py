from game.anx.BulletIdLogic import BulletIdLogic
from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.LinearRandomGenerator import LinearRandomGenerator
from game.lib.Math import Math


class DebrisLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletIdLogic: BulletIdLogic,
    ):
        self.traversal = traversal
        self.bulletIdLogic = bulletIdLogic

    def makeDebrisFromExplosion(self, gameState, explosion):
        if explosion.debrisType is None:
            return None

        currentLevelSegment = self.traversal.findLevelSegment(gameState.collisionTree, explosion.position)
        visibilityLevelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, explosion.position)

        debris = self.makeDebrisWithRandomPositions(explosion)
        for piece in debris:
            self.addToGameState(gameState, piece, currentLevelSegment, visibilityLevelSegment)

    def makeDebrisManually(self, gameState, id, debrisType, ownerPerson, position, direction):
        currentLevelSegment = self.traversal.findLevelSegment(gameState.collisionTree, position)
        visibilityLevelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, position)

        piece = debrisType()
        piece.id = id
        piece.currentPosition = position.copy()
        piece.nextPosition = piece.currentPosition.copy()
        piece.direction = direction.copy()
        piece.velocity = piece.direction.copy()
        piece.velocity.setLength(piece.velocityValue)
        piece.ownerPerson = ownerPerson

        self.addToGameState(gameState, piece, currentLevelSegment, visibilityLevelSegment)

        return piece

    def addToGameState(self, gameState, piece, currentLevelSegment, visibilityLevelSegment):
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

    def makeDebrisWithRandomPositions(self, explosion):
        # позиции осколков не передаются между клиентом и сервером
        # для восстановления позиций на принимающей стороне используется randomSeed сгенерированный при создании пули

        assert explosion.debrisCount <= CommonConstants.maxDebrisCount
        result = []
        rand = LinearRandomGenerator(explosion.bullet.randomSeed)
        for n in range(0, explosion.debrisCount):
            piece = explosion.debrisType()
            piece.id = self.bulletIdLogic.getDebrisPieceId(explosion.bullet.id, n)
            piece.currentPosition = explosion.position.copy()
            piece.nextPosition = piece.currentPosition.copy()
            planeNormal = Vector3(rand.getFloat(-0.1, 0.1), rand.getFloat(-0.1, 0.1), 1.0)
            planeNormal.normalize()
            plane = Plane(planeNormal, CommonConstants.axisOrigin)
            piece.direction = Geometry.rotatePoint(
                plane.getAnyVector(), planeNormal, CommonConstants.axisOrigin, rand.getFloat(-Math.piDouble, Math.piDouble)
            )
            piece.direction.normalize()
            piece.velocity = piece.direction.copy()
            piece.velocity.setLength(piece.velocityValue)
            piece.ownerPerson = explosion.bullet.ownerPerson
            result.append(piece)

        return result
