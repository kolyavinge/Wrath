from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(
        self,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
    ):
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def updateForPlayers(self, gameState):
        for player in gameState.players:
            self.updateForPerson(player, gameState.collisionTree, gameState.visibilityTree)

    def updateForPlayer(self, gameState):
        player = gameState.player
        self.updateForPerson(player, gameState.collisionTree, gameState.visibilityTree)

    def updateForPerson(self, person, collisionTree, visibilityTree):
        self.removePlayerFromLevelSegments(person)
        self.personLevelSegmentsUpdater.updatePerson(person, collisionTree, visibilityTree)
        self.addPlayerToLevelSegments(person)

    def removePlayerFromLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.remove(player)

    def addPlayerToLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.append(player)
