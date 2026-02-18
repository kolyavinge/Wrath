from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector


class PersonCollisionUpdater:

    def __init__(
        self,
        personCollisionDetector: PersonCollisionDetector,
    ):
        self.personCollisionDetector = personCollisionDetector

    def update(self, gameState):
        for levelSegment in gameState.collisionTree.allLevelSegments:
            for person1 in levelSegment.allPerson:
                for person2 in levelSegment.allPerson:
                    if person1 != person2:
                        if person1.hasMoved or person2.hasMoved:
                            self.updateForPerson(gameState, person1, person2)

    def updateForPerson(self, gameState, person1, person2):
        collisionLength = self.personCollisionDetector.getCollisionLengthOrNone(person1, person2)
        if collisionLength is not None:
            velocitySum = person1.velocityValue + person2.velocityValue
            if velocitySum > 0:
                self.movePerson(person1, collisionLength, velocitySum)
                self.movePerson(person2, collisionLength, velocitySum)
                gameState.collisionData.personPerson[person1] = person2
                gameState.collisionData.personPerson[person2] = person1

    def movePerson(self, person, collisionLength, velocitySum):
        if person.hasMoved:
            personCollisionLength = collisionLength * person.velocityValue / velocitySum
            if personCollisionLength > 0:
                collisionVelocity = person.velocityVector.copy()
                collisionVelocity.setLength(personCollisionLength)
                collisionVelocity.mul(-1)
                person.moveNextPositionBy(collisionVelocity)
