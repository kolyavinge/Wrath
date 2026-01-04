from game.engine.GameState import GameState
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random


class PersonRespawnUpdater:

    def __init__(
        self,
        gameState: GameState,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameState = gameState
        self.personTurnLogic = personTurnLogic

    def update(self):
        if len(self.gameState.respawnRequests) == 0:
            return

        for person in self.gameState.respawnRequests:
            self.generateRespawnPosition(person)

        self.gameState.respawnRequests.clear()

    def generateRespawnPosition(self, person):
        respawnArea = Random.getListItem(self.gameState.level.respawnAreas)
        position = respawnArea.getRandomPoint()
        person.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(person, respawnArea.frontNormal)
        person.hasMoved = True
        person.hasTurned = True
