from game.audio.AudioPlayer import AudioPlayer
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PlayertemsAudioSources import PlayertemsAudioSources


class PlayerItemsVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
    ):
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer

    def init(self, gameState, allSources):
        self.source = PlayertemsAudioSources(gameState.player, self.audioSourceFactory)
        allSources.append(self.source)

    def vox(self, updateStatistic):
        if updateStatistic.isSwitchedTorch:
            self.audioPlayer.play(self.source.switchTorch)
