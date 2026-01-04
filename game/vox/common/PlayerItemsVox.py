from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameState import GameState
from game.lib.EventManager import EventManager, Events
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PlayertemsAudioSources import PlayertemsAudioSources


class PlayerItemsVox:

    def __init__(
        self,
        gameState: GameState,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.torchSwitched, self.onTorchSwitched)

    def init(self, allSources):
        self.source = PlayertemsAudioSources(self.gameState.player, self.audioSourceFactory)
        allSources.append(self.source)

    def onTorchSwitched(self, _):
        self.audioPlayer.play(self.source.switchTorch)
