class PlayerBreathUpdater:

    def update(self, gameState):
        player = gameState.player
        currentWeapon = gameState.playerItems.currentWeapon
        if not currentWeapon.isFiring:
            player.breathTime += 1.0
        else:
            player.breathTime = 0
