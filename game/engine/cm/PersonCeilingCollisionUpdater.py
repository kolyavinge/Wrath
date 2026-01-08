from game.anx.PersonConstants import PersonConstants
from game.engine.cm.PersonCeilingCollisionDetector import PersonCeilingCollisionDetector
from game.engine.GameState import GameState
from game.model.person.PersonStates import PersonZState


class PersonCeilingCollisionUpdater:

    def __init__(
        self,
        gameState: GameState,
        personCeilingCollisionDetector: PersonCeilingCollisionDetector,
    ):
        self.gameState = gameState
        self.personCeilingCollisionDetector = personCeilingCollisionDetector

    def updateForPlayer(self):
        self.updateForPerson(self.gameState.player)

    def updateForEnemies(self):
        for enemy in self.gameState.enemies:
            self.updateForPerson(enemy)

    def updateForPerson(self, person):
        if person.zState == PersonZState.jumping:
            ceiling = self.personCeilingCollisionDetector.getCollidedCeilingOrNone(person)
            if ceiling is not None:
                person.setZ(ceiling.downLeft.z - PersonConstants.zLength)
