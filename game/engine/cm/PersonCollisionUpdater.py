from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.GameState import GameState


class PersonCollisionUpdater:

    def __init__(
        self,
        gameData: GameState,
        personCollisionDetector: PersonCollisionDetector,
    ):
        self.gameData = gameData
        self.personCollisionDetector = personCollisionDetector

    def update(self):
        for person1, person2 in self.gameData.allPersonPairs:
            if person1.hasMoved or person2.hasMoved:
                self.updateForPerson(person1, person2)

    def updateForPerson(self, person1, person2):
        collisionLength = self.personCollisionDetector.getCollisionLengthOrNone(person1, person2)
        if collisionLength is not None:
            velocitySum = person1.velocityValue + person2.velocityValue
            self.movePerson(person1, collisionLength, velocitySum)
            self.movePerson(person2, collisionLength, velocitySum)
            self.gameData.collisionData.personPerson[person1] = person2
            self.gameData.collisionData.personPerson[person2] = person1

    def movePerson(self, person, collisionLength, velocitySum):
        if person.hasMoved:
            personCollisionLength = collisionLength * person.velocityValue / velocitySum
            collisionVelocity = person.velocityVector.copy()
            collisionVelocity.setLength(personCollisionLength)
            collisionVelocity.mul(-1)
            person.moveNextPositionBy(collisionVelocity)
