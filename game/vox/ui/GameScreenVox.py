from game.audio.AudioPlayer import AudioPlayer
from game.vox.common.PersonVox import PersonVox
from game.vox.common.PlayerItemsVox import PlayerItemsVox
from game.vox.common.PowerupVox import PowerupVox
from game.vox.common.WeaponVox import WeaponVox


class GameScreenVox:

    def __init__(
        self,
        audioPlayer: AudioPlayer,
        personVox: PersonVox,
        playerItemsVox: PlayerItemsVox,
        weaponVox: WeaponVox,
        powerupVox: PowerupVox,
    ):
        self.allSources = []
        self.audioPlayer = audioPlayer
        self.personVox = personVox
        self.playerItemsVox = playerItemsVox
        self.weaponVox = weaponVox
        self.powerupVox = powerupVox

    def init(self, gameState):
        for source in self.allSources:
            source.release()

        self.allSources = []
        self.personVox.init(gameState, self.allSources)
        self.playerItemsVox.init(gameState, self.allSources)
        self.weaponVox.init(gameState, self.allSources)
        self.powerupVox.init(gameState, self.allSources)

    def update(self, gameState):
        self.audioPlayer.setListenerPosition(gameState.player.currentCenterPoint)
        for source in self.allSources:
            source.updatePosition()
