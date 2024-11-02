from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector


class BulletCollisionDetector:

    def __init__(self, constructionCollisionDetector):
        self.constructionCollisionDetector = constructionCollisionDetector

    def getConstructionCollisionResultOrNone(self, bullet):
        result = self.constructionCollisionDetector.getConstructionCollisionResultOrNone(
            bullet.currentLevelSegment, bullet.currentPosition, bullet.nextPosition
        )

        return result


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector(resolver.resolve(ConstructionCollisionDetector))
