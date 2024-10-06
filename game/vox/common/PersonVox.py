from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.audio.AudioSourceLoader import AudioSourceLoader
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioBufferCollection import AudioBufferCollection
from game.vox.sources.PersonAudioSources import PersonAudioSources


class PersonVox:

    def __init__(self, gameData, audioBufferCollection, audioSourceLoader, audioPlayer, eventManager):
        self.sources = {}
        self.gameData = gameData
        self.audioBufferCollection = audioBufferCollection
        self.audioSourceLoader = audioSourceLoader
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.personStepDone, self.onPersonStepDone)

    def init(self):
        for source in self.sources.values():
            source.release()

        self.sources = {}
        self.sources[self.gameData.player] = PersonAudioSources(self.gameData.player, self.audioBufferCollection, self.audioSourceLoader)
        # other enemies

    def onPersonStepDone(self, person):
        source = self.sources[person]
        self.audioPlayer.play(source.step)

    def update(self):
        for source in self.sources.values():
            source.updatePosition()


def makePersonVox(resolver):
    return PersonVox(
        resolver.resolve(GameData),
        resolver.resolve(AudioBufferCollection),
        resolver.resolve(AudioSourceLoader),
        resolver.resolve(AudioPlayer),
        resolver.resolve(EventManager),
    )
