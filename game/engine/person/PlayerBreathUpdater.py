from game.engine.GameState import GameState


class PlayerBreathUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        player = self.gameState.player
        currentWeapon = self.gameState.playerItems.currentWeapon
        if not player.hasMoved and not currentWeapon.isFiring:
            player.breathTime += 1.0
        else:
            player.breathTime = 0
