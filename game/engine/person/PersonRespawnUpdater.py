from game.anx.PersonConstants import PersonConstants
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.person.PersonStates import LifeCycle


class PersonRespawnUpdater:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
    ):
        self.personTurnLogic = personTurnLogic

    def update(self, gameState):
        for person in gameState.allPerson:
            if person.lifeCycle == LifeCycle.respawn:
                self.respawn(person, gameState.level.respawnAreas)

    def respawn(self, person, respawnAreas):
        respawnArea = Random.getListItem(respawnAreas)
        position = respawnArea.getRandomPoint()
        person.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(person, respawnArea.frontNormal)
        person.hasMoved = True
        person.hasTurned = True
        person.commitNextPosition()
        person.addHealth(PersonConstants.maxPersonHealth)
