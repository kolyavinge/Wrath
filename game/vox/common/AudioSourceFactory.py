from game.audio.AudioSourceLoader import AudioSourceLoader
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class AudioSourceFactory:

    def __init__(self, audioSourceLoader, audioBufferCollection):
        self.audioSourceLoader = audioSourceLoader
        self.audioBufferCollection = audioBufferCollection

    def getSelectMenuItem(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.selectMenuItem)

    def getStep(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.step)

    def getTorchSwitch(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.torchSwitch)


def makeAudioSourceFactory(resolver):
    return AudioSourceFactory(resolver.resolve(AudioSourceLoader), resolver.resolve(AudioBufferCollection))
