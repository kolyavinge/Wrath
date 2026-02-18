from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(
        self,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
    ):
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def update(self, gameState):
        player = gameState.player
        self.removePlayerFromLevelSegments(player)
        self.personLevelSegmentsUpdater.updatePerson(player, gameState.collisionTree, gameState.visibilityTree)
        self.addPlayerToLevelSegments(player)

    def removePlayerFromLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.remove(player)

    def addPlayerToLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.append(player)
