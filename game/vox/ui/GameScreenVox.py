from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.vox.common.PersonVox import PersonVox
from game.vox.common.PlayerItemsVox import PlayerItemsVox
from game.vox.common.PowerupVox import PowerupVox
from game.vox.common.WeaponVox import WeaponVox


class GameScreenVox:

    def __init__(
        self,
        gameData: GameData,
        audioPlayer: AudioPlayer,
        personVox: PersonVox,
        playerItemsVox: PlayerItemsVox,
        weaponVox: WeaponVox,
        powerupVox: PowerupVox,
    ):
        self.allSources = []
        self.gameData = gameData
        self.audioPlayer = audioPlayer
        self.personVox = personVox
        self.playerItemsVox = playerItemsVox
        self.weaponVox = weaponVox
        self.powerupVox = powerupVox

    def init(self):
        for source in self.allSources:
            source.release()

        self.allSources = []
        self.personVox.init(self.allSources)
        self.playerItemsVox.init(self.allSources)
        self.weaponVox.init(self.allSources)
        self.powerupVox.init(self.allSources)

    def update(self):
        self.audioPlayer.setListenerPosition(self.gameData.player.currentCenterPoint)
        for source in self.allSources:
            source.updatePosition()
