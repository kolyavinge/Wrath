from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PlayertemsAudioSources import PlayertemsAudioSources


class PlayerItemsVox:

    def __init__(self, gameData, audioSourceFactory, audioPlayer, eventManager):
        self.gameData = gameData
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.torchSwitched, self.onTorchSwitched)

    def init(self, allSources):
        self.source = PlayertemsAudioSources(self.gameData.player, self.audioSourceFactory)
        allSources.append(self.source)

    def onTorchSwitched(self, _):
        self.audioPlayer.play(self.source.switchTorch)


def makePlayerItemsVox(resolver):
    return PlayerItemsVox(
        resolver.resolve(GameData),
        resolver.resolve(AudioSourceFactory),
        resolver.resolve(AudioPlayer),
        resolver.resolve(EventManager),
    )
