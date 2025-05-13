from game.anx.PersonConstants import PersonConstants


class PersonCollisionDetector:

    def getCollisionLengthOrNone(self, person1, person2):
        return self.getCollisionLengthBetweenPointsOrNone(person1.nextCenterPoint, person2.nextCenterPoint)

    def getCollisionLengthBetweenPointsOrNone(self, point1, point2):
        # пересечение окружностей
        collisionLength = PersonConstants.xyLength - point1.getLengthTo(point2)
        return collisionLength if collisionLength > 0 else None
