from game.audio import AudioSourceLoader
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class AudioSourceCollection:

    def __init__(self, audioBufferCollection, audioSourceLoader):
        self.audioBufferCollection = audioBufferCollection
        self.audioSourceLoader = audioSourceLoader

    def init(self):
        self.selectMenuItem = self.audioSourceLoader.load(self.audioBufferCollection.selectMenuItem)


def makeAudioSourceCollection(resolver):
    return AudioSourceCollection(resolver.resolve(AudioBufferCollection), resolver.resolve(AudioSourceLoader))
