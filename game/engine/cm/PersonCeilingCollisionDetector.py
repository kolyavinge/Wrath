from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector


class PersonCeilingCollisionDetector:

    def __init__(self, constructionCollisionDetector: ConstructionCollisionDetector):
        self.constructionCollisionDetector = constructionCollisionDetector

    def getCollidedCeilingOrNone(self, person):
        for levelSegments in person.collisionLevelSegments:
            startPoint = person.currentBorder.top.center
            endPoint = person.nextBorder.top.center
            ceiling = self.constructionCollisionDetector.getCollidedConstructionOrNone(levelSegments.ceilings, startPoint, endPoint)
            if ceiling is not None:
                return ceiling

        return None
