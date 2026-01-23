from game.model.person.PersonStates import PersonZState


class PersonPositionUpdater:

    def movePlayerNextPosition(self, gameState):
        self.movePersonNextPosition(gameState.player)

    def moveEnemiesNextPosition(self, gameState):
        for enemy in gameState.enemies:
            self.movePersonNextPosition(enemy)

    def movePersonNextPosition(self, person):
        if person.velocityValue > 0:
            person.hasMoved = True
            person.moveNextPositionBy(person.velocityVector)

    def commitPlayerNextPosition(self, gameState):
        if gameState.player.hasMoved:
            gameState.player.commitNextPosition()

    def commitEnemiesNextPosition(self, gameState):
        for enemy in gameState.enemies:
            if enemy.hasMoved:
                enemy.commitNextPosition()

    def resetMovedAndTurnedForPlayer(self, gameState):
        player = gameState.player
        player.hasTurned = False
        if player.hasMoved and player.zState == PersonZState.onFloor:
            player.hasMoved = False

    def resetMovedAndTurned(self, gameState):
        for person in gameState.allPerson:
            person.hasTurned = False
            if person.hasMoved and person.zState == PersonZState.onFloor:
                person.hasMoved = False
