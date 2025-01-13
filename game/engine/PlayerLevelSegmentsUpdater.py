from game.engine.GameData import GameData
from game.engine.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(self, gameData, personLevelSegmentsUpdater):
        self.gameData = gameData
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def updateIfMoved(self):
        if self.gameData.player.hasMoved:
            self.update()

    def update(self):
        self.personLevelSegmentsUpdater.updatePerson(self.gameData.player)


def makePlayerLevelSegmentsUpdater(resolver):
    return PlayerLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(PersonLevelSegmentsUpdater))
