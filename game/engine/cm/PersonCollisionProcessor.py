from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.GameData import GameData


class PersonCollisionProcessor:

    def __init__(self, gameData, personCollisionDetector):
        self.gameData = gameData
        self.personCollisionDetector = personCollisionDetector

    def process(self):
        for person1, person2 in self.gameData.allPersonPairs:
            if person1.hasMoved or person2.hasMoved:
                self.processPerson(person1, person2)

    def processPerson(self, person1, person2):
        collisionLength = self.personCollisionDetector.getCollisionLengthOrNone(person1, person2)
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


def makePersonCollisionProcessor(resolver):
    return PersonCollisionProcessor(resolver.resolve(GameData), resolver.resolve(PersonCollisionDetector))
