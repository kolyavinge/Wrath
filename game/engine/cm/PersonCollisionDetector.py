from game.anx.PersonConstants import PersonConstants


class PersonCollisionDetector:

    def getCollisionLengthOrNone(self, person1, person2):
        # пересечение окружностей
        collisionLength = PersonConstants.xyLength - person1.nextCenterPoint.getLengthTo(person2.nextCenterPoint)
        return collisionLength if collisionLength > 0 else None


def makePersonCollisionDetector(resolver):
    return PersonCollisionDetector()
