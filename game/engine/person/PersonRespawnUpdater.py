from game.anx.PersonConstants import PersonConstants
from game.engine.GameState import GameState
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.person.PersonStates import LifeCycle


class PersonRespawnUpdater:

    def __init__(
        self,
        gameState: GameState,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameState = gameState
        self.personTurnLogic = personTurnLogic

    def update(self):
        for person in self.gameState.allPerson:
            if person.lifeCycle == LifeCycle.respawn:
                self.respawn(person)

    def respawn(self, person):
        respawnArea = Random.getListItem(self.gameState.level.respawnAreas)
        position = respawnArea.getRandomPoint()
        person.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(person, respawnArea.frontNormal)
        person.hasMoved = True
        person.hasTurned = True
        person.commitNextPosition()
        person.addHealth(PersonConstants.maxPersonHealth)
