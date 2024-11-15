from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupAudioSources:

    def __init__(self, player, audioSourceFactory):
        self.player = player
        self.powerups = {}
        self.powerups[WeaponPowerup] = audioSourceFactory.makeWeaponPickup()
        self.powerups[WeaponPowerup].setGain(0.6)

    def updatePosition(self):
        position = self.player.currentCenterPoint
        for powerup in self.powerups.values():
            powerup.setPosition(position)

    def release(self):
        for powerup in self.powerups.values():
            powerup.release()
