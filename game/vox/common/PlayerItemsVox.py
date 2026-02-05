from game.audio.AudioPlayer import AudioPlayer
from game.lib.EventManager import EventManager, Events
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PlayertemsAudioSources import PlayertemsAudioSources


class PlayerItemsVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
        eventManager: EventManager,
    ):
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.torchSwitchRequested, self.switchTorch)

    def init(self, gameState, allSources):
        self.source = PlayertemsAudioSources(gameState.player, self.audioSourceFactory)
        allSources.append(self.source)

    def vox(self, updateStatistic):
        pass

    def switchTorch(self, torch):
        self.audioPlayer.play(self.source.switchTorch)
