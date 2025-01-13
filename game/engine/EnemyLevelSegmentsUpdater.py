from game.engine.GameData import GameData
from game.engine.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater


class EnemyLevelSegmentsUpdater:

    def __init__(self, gameData, personLevelSegmentsUpdater):
        self.gameData = gameData
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

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

    def removeEnemyFromLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.remove(enemy)

        if enemy in enemy.visibilityLevelSegment.enemies:
            enemy.visibilityLevelSegment.enemies.remove(enemy)

    def addEnemyToLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.append(enemy)

        enemy.visibilityLevelSegment.enemies.append(enemy)


def makeEnemyLevelSegmentsUpdater(resolver):
    return EnemyLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(PersonLevelSegmentsUpdater))
