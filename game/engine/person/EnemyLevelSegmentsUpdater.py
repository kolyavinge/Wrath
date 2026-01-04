from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class EnemyLevelSegmentsUpdater:

    def __init__(
        self,
        gameData: GameState,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater
        self.traversal = traversal

    def updateIfMoved(self):
        for enemy in self.gameData.enemies:
            if enemy.hasMoved:
                self.updateEnemy(enemy)

    def update(self):
        for enemy in self.gameData.enemies:
            self.updateEnemy(enemy)

    def updateEnemy(self, enemy):
        self.removeEnemyFromLevelSegments(enemy)
        self.personLevelSegmentsUpdater.updatePerson(enemy)
        self.addEnemyToLevelSegments(enemy)
        self.updateCurrentCenterPointLevelSegment(enemy)

    def removeEnemyFromLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.remove(enemy)
            segment.allPerson.remove(enemy)

        if enemy in enemy.visibilityLevelSegment.enemies:
            enemy.visibilityLevelSegment.enemies.remove(enemy)
            enemy.visibilityLevelSegment.allPerson.remove(enemy)

    def addEnemyToLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.append(enemy)
            segment.allPerson.append(enemy)

        enemy.visibilityLevelSegment.enemies.append(enemy)
        enemy.visibilityLevelSegment.allPerson.append(enemy)

    def updateCurrentCenterPointLevelSegment(self, enemy):
        bspTree = self.gameData.collisionTree
        enemy.currentCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, enemy.currentCenterPoint)
