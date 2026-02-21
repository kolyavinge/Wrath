from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class PlayerLevelSegmentsUpdater:

    def __init__(
        self,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
        traversal: BSPTreeTraversal,
    ):
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater
        self.traversal = traversal

    def updateForAllPerson(self, gameState):
        for person in gameState.allPerson:
            self.updateForPerson(person, gameState.collisionTree, gameState.visibilityTree)

    def updateForPlayer(self, gameState):
        player = gameState.player
        self.updateForPerson(player, gameState.collisionTree, gameState.visibilityTree)

    def updateForPerson(self, person, collisionTree, visibilityTree):
        self.removePlayerFromLevelSegments(person)
        self.personLevelSegmentsUpdater.updatePerson(person, collisionTree, visibilityTree)
        self.addPlayerToLevelSegments(person)
        person.currentCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(collisionTree, person.currentCenterPoint)

    def removePlayerFromLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.remove(player)

    def addPlayerToLevelSegments(self, player):
        for segment in player.collisionLevelSegments:
            segment.allPerson.append(player)
