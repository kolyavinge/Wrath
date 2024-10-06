from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.audio.AudioSourceLoader import AudioSourceLoader
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioBufferCollection import AudioBufferCollection
from game.vox.sources.PlayertemsAudioSources import PlayertemsAudioSources


class PlayerItemsVox:

    def __init__(self, gameData, audioBufferCollection, audioSourceLoader, audioPlayer, eventManager):
        self.gameData = gameData
        self.audioBufferCollection = audioBufferCollection
        self.audioSourceLoader = audioSourceLoader
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.torchSwitched, self.onTorchSwitched)

    def init(self, allSources):
        self.source = PlayertemsAudioSources(self.gameData.player, self.audioBufferCollection, self.audioSourceLoader)
        allSources.append(self.source)

    def onTorchSwitched(self, _):
        self.audioPlayer.play(self.source.torchSwitch)


def makePlayerItemsVox(resolver):
    return PlayerItemsVox(
        resolver.resolve(GameData),
        resolver.resolve(AudioBufferCollection),
        resolver.resolve(AudioSourceLoader),
        resolver.resolve(AudioPlayer),
        resolver.resolve(EventManager),
    )
