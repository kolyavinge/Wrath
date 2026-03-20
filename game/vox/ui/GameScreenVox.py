from game.vox.common.ExplosionVox import ExplosionVox
from game.vox.common.PersonVox import PersonVox
from game.vox.common.PlayerItemsVox import PlayerItemsVox
from game.vox.common.PowerupVox import PowerupVox
from game.vox.common.WeaponVox import WeaponVox
from game.vox.lib.AudioPlayer import AudioPlayer


class GameScreenVox:

    def __init__(
        self,
        audioPlayer: AudioPlayer,
        personVox: PersonVox,
        playerItemsVox: PlayerItemsVox,
        weaponVox: WeaponVox,
        explosionVox: ExplosionVox,
        powerupVox: PowerupVox,
    ):
        self.allSources = []
        self.audioPlayer = audioPlayer
        self.personVox = personVox
        self.playerItemsVox = playerItemsVox
        self.weaponVox = weaponVox
        self.explosionVox = explosionVox
        self.powerupVox = powerupVox

    def init(self, gameState):
        for source in self.allSources:
            source.release()

        self.allSources = []
        self.personVox.init(gameState, self.allSources)
        self.playerItemsVox.init(gameState, self.allSources)
        self.weaponVox.init(gameState, self.allSources)
        self.explosionVox.init(self.allSources)
        self.powerupVox.init(gameState, self.allSources)

    def update(self, gameState):
        self.audioPlayer.setListenerPosition(gameState.player.currentCenterPoint, gameState.player.lookDirection)

        for source in self.allSources:
            source.updatePosition()

        self.personVox.vox(gameState.updateStatistic)
        self.playerItemsVox.vox(gameState.updateStatistic)
        self.weaponVox.vox(gameState.updateStatistic)
        self.explosionVox.vox(gameState.updateStatistic)
        self.powerupVox.vox(gameState.updateStatistic)
