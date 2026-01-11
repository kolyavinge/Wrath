from game.engine.GameState import GameState


class PersonUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def commitZStateForPlayer(self):
        self.gameState.player.prevZState = self.gameState.player.zState

    def commitZStateForEnemies(self):
        for enemy in self.gameState.enemies:
            enemy.prevZState = enemy.zState

    def updateDelaysForPlayer(self):
        self.gameState.player.paralyzeDelay.decrease()

    def updateDelaysForEnemies(self):
        for enemy in self.gameState.enemies:
            enemy.paralyzeDelay.decrease()
