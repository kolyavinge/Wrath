from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData


class PersonCollisionProcessor:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        for person1, person2 in self.gameData.allPersonPairs:
            if person1.hasMoved or person2.hasMoved:
                self.processPerson(person1, person2)

    def processPerson(self, person1, person2):
        collisionLength = self.getCollisionLengthOrNone(person1, person2)
        if collisionLength is not None:
            velocitySum = person1.velocityValue + person2.velocityValue
            self.movePerson(person1, collisionLength, velocitySum)
            self.movePerson(person2, collisionLength, velocitySum)

    def movePerson(self, person, collisionLength, velocitySum):
        if person.hasMoved:
            personCollisionLength = collisionLength * person.velocityValue / velocitySum
            collisionVelocity = person.velocityVector.copy()
            collisionVelocity.setLength(personCollisionLength)
            collisionVelocity.mul(-1)
            person.moveNextPositionBy(collisionVelocity)

    def getCollisionLengthOrNone(self, person1, person2):
        # пересечение окружностей
        collisionLength = PersonConstants.xyLength - person1.nextCenterPoint.getLengthTo(person2.nextCenterPoint)
        return collisionLength if collisionLength > 0 else None


def makePersonCollisionProcessor(resolver):
    return PersonCollisionProcessor(resolver.resolve(GameData))
