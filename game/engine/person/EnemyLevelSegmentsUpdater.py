from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class EnemyLevelSegmentsUpdater:

    def __init__(
        self,
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
        traversal: BSPTreeTraversal,
    ):
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater
        self.traversal = traversal

    def updateIfMoved(self, gameState):
        for enemy in gameState.enemies:
            if enemy.hasMoved:
                self.updateEnemy(enemy, gameState.collisionTree)

    def update(self, gameState):
        for enemy in gameState.enemies:
            self.updateEnemy(enemy, gameState.collisionTree)

    def updateEnemy(self, enemy, collisionTree):
        self.removeEnemyFromLevelSegments(enemy)
        self.personLevelSegmentsUpdater.updatePerson(enemy)
        self.addEnemyToLevelSegments(enemy)
        enemy.currentCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(collisionTree, enemy.currentCenterPoint)

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
