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

    def updateForBots(self, gameState):
        for bot in gameState.bots:
            self.updateForPerson(bot)

    def updateForPerson(self, person):
        if person.zState == PersonZState.jumping:
            ceiling = self.personCeilingCollisionDetector.getCollidedCeilingOrNone(person)
            if ceiling is not None:
                person.setZ(ceiling.downLeft.z - PersonConstants.zLength)
