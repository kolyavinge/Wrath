from game.engine.GameState import GameState
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(
        self,
        gameState: GameState,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
    ):
        self.gameState = gameState
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def updateIfMoved(self):
        if self.gameState.player.hasMoved:
            self.update()

    def update(self):
        self.removePlayerFromLevelSegments(self.gameState.player)
        self.personLevelSegmentsUpdater.updatePerson(self.gameState.player)
        self.addPlayerToLevelSegments(self.gameState.player)

    def removePlayerFromLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.remove(player)

    def addPlayerToLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.append(player)
