class PersonUpdater:

    def commitZStateForPlayer(self, gameState):
        gameState.player.prevZState = gameState.player.zState

    def commitZStateForEnemies(self, gameState):
        for enemy in gameState.enemies:
            enemy.prevZState = enemy.zState

    def updateDelaysForPlayer(self, gameState):
        gameState.player.paralyzeDelay.decrease()

    def updateDelaysForEnemies(self, gameState):
        for enemy in gameState.enemies:
            enemy.paralyzeDelay.decrease()
