from game.engine.GameState import GameState
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(
        self,
        gameData: GameState,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
    ):
        self.gameData = gameData
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def updateIfMoved(self):
        if self.gameData.player.hasMoved:
            self.update()

    def update(self):
        self.removePlayerFromLevelSegments(self.gameData.player)
        self.personLevelSegmentsUpdater.updatePerson(self.gameData.player)
        self.addPlayerToLevelSegments(self.gameData.player)

    def removePlayerFromLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.enemies.remove(player)
            segment.allPerson.remove(player)

    def addPlayerToLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.enemies.append(player)
            segment.allPerson.append(player)
