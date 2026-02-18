class PersonPositionUpdater:

    def movePlayerNextPosition(self, gameState):
        self.movePersonNextPosition(gameState.player)

    def moveEnemiesNextPosition(self, gameState):
        for enemy in gameState.enemies:
            self.movePersonNextPosition(enemy)

    def movePersonNextPosition(self, person):
        if person.velocityValue > 0:
            person.moveNextPositionBy(person.velocityVector)

    def commitPlayerNextPosition(self, gameState):
        gameState.player.commitNextPosition()

    def commitEnemiesNextPosition(self, gameState):
        for enemy in gameState.enemies:
            enemy.commitNextPosition()
