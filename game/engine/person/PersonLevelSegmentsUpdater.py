from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class PersonLevelSegmentsUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def updateForAllPerson(self, gameState):
        for person in gameState.allPerson:
            self.updateForPerson(person, gameState.collisionTree, gameState.visibilityTree)

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.collisionTree, gameState.visibilityTree)

    def updateForEnemies(self, gameState):
        for enemy in gameState.enemies:
            self.updateEnemy(enemy, gameState)

    def updateForPerson(self, person, collisionTree, visibilityTree):
        self.removePersonFromLevelSegments(person)
        self.updatePerson(person, collisionTree, visibilityTree)
        self.addPersonToLevelSegments(person)
        person.currentCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(collisionTree, person.currentCenterPoint)

    def updateEnemy(self, enemy, gameState):
        self.removeEnemyFromLevelSegments(enemy)
        self.updatePerson(enemy, gameState.collisionTree, gameState.visibilityTree)
        self.addEnemyToLevelSegments(enemy)

    def updatePerson(self, person, collisionTree, visibilityTree):
        person.collisionLevelSegments = set()
        self.updateCollisionLevelSegments(person, collisionTree, person.currentBorder.bottom)
        self.updateCollisionLevelSegments(person, collisionTree, person.currentBorder.top)
        person.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(visibilityTree, person.currentCenterPoint)

    def updateCollisionLevelSegments(self, person, bspTree, border):
        segments = person.collisionLevelSegments
        segments.add(self.traversal.findLevelSegmentOrNone(bspTree, border.downLeft))
        segments.add(self.traversal.findLevelSegmentOrNone(bspTree, border.downRight))
        segments.add(self.traversal.findLevelSegmentOrNone(bspTree, border.upLeft))
        segments.add(self.traversal.findLevelSegmentOrNone(bspTree, border.upRight))

    def addPersonToLevelSegments(self, person):
        for segment in person.collisionLevelSegments:
            segment.allPerson.append(person)

    def removePersonFromLevelSegments(self, person):
        for segment in person.collisionLevelSegments:
            segment.allPerson.remove(person)

    def addEnemyToLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.append(enemy)
            segment.allPerson.append(enemy)

        enemy.visibilityLevelSegment.enemies.append(enemy)
        enemy.visibilityLevelSegment.allPerson.append(enemy)

    def removeEnemyFromLevelSegments(self, enemy):
        for segment in enemy.collisionLevelSegments:
            segment.enemies.remove(enemy)
            segment.allPerson.remove(enemy)

        if enemy in enemy.visibilityLevelSegment.enemies:
            enemy.visibilityLevelSegment.enemies.remove(enemy)
            enemy.visibilityLevelSegment.allPerson.remove(enemy)
