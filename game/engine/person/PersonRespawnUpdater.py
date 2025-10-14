from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random


class PersonRespawnUpdater:

    def __init__(
        self,
        gameData: GameData,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic

    def update(self):
        if len(self.gameData.respawnRequests) == 0:
            return

        for person in self.gameData.respawnRequests:
            self.generateRespawnPosition(person)

        self.gameData.respawnRequests.clear()

    def generateRespawnPosition(self, person):
        respawnArea = Random.getListItem(self.gameData.level.respawnAreas)
        position = respawnArea.getRandomPoint()
        person.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(person, respawnArea.frontNormal)
        person.hasMoved = True
        person.hasTurned = True
