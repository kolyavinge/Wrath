from game.audio.AudioPlayer import AudioPlayer
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PowerupAudioSources import PowerupAudioSources


class PowerupVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
    ):
        self.sources = {}
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer

    def init(self, gameState, allSources):
        self.source = PowerupAudioSources(gameState.player, self.audioSourceFactory)
        allSources.append(self.source)

    def vox(self, updateStatistic):
        for powerup in updateStatistic.pickedUpPowerups:
            self.audioPlayer.play(self.source.powerups[type(powerup)])
