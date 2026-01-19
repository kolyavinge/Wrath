class PlayerBreathUpdater:

    def update(self, gameState):
        player = gameState.player
        currentWeapon = gameState.playerItems.currentWeapon
        if not player.hasMoved and not currentWeapon.isFiring:
            player.breathTime += 1.0
        else:
            player.breathTime = 0
