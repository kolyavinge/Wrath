from game.anx.PersonConstants import PersonConstants
from game.engine.cm.PersonCeilingCollisionDetector import PersonCeilingCollisionDetector
from game.model.person.PersonStates import PersonZState


class PersonCeilingCollisionUpdater:

    def __init__(
        self,
        personCeilingCollisionDetector: PersonCeilingCollisionDetector,
    ):
        self.personCeilingCollisionDetector = personCeilingCollisionDetector

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player)

    def updateForEnemies(self, gameState):
        for enemy in gameState.enemies:
            self.updateForPerson(enemy)

    def updateForPerson(self, person):
        if person.zState == PersonZState.jumping:
            ceiling = self.personCeilingCollisionDetector.getCollidedCeilingOrNone(person)
            if ceiling is not None:
                person.setZ(ceiling.downLeft.z - PersonConstants.zLength)
