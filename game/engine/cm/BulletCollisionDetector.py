from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.GameData import GameData


class BulletCollisionDetector:

    def __init__(self, gameData, constructionCollisionDetector, traversal):
        self.gameData = gameData
        self.constructionCollisionDetector = constructionCollisionDetector
        self.traversal = traversal

    def getConstructionCollisionResultOrNone(self, bullet):
        return self.getResultRec(bullet.currentLevelSegment, bullet.nextLevelSegment, bullet.currentPosition, bullet.nextPosition)

    def getResultRec(self, startSegment, endSegment, startPoint, endPoint):
        if startSegment == endSegment:
            return self.constructionCollisionDetector.getConstructionCollisionResultOrNone(startSegment, startPoint, endPoint)
        else:
            direction = startPoint.getDirectionTo(endPoint)
            if direction.getLength() < 1.0:
                return self.constructionCollisionDetector.getConstructionCollisionResultOrNone(
                    startSegment, startPoint, endPoint
                ) or self.constructionCollisionDetector.getConstructionCollisionResultOrNone(endSegment, startPoint, endPoint)
            else:
                direction.div(2)
                middlePoint = startPoint.copy()
                middlePoint.add(direction)
                middleSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.collisionTree, middlePoint)
                return self.getResultRec(startSegment, middleSegment, startPoint, middlePoint) or self.getResultRec(
                    middleSegment, endSegment, middlePoint, endPoint
                )


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector(resolver.resolve(GameData), resolver.resolve(ConstructionCollisionDetector), resolver.resolve(BSPTreeTraversal))
