from game.audio.AudioBufferLoader import AudioBufferLoader
from game.lib.Environment import Environment


class AudioBufferCollection:

    def __init__(self, audioBufferLoader):
        self.audioBufferLoader = audioBufferLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\audio\\"
        self.selectMenuItem = self.audioBufferLoader.load(path + "selectMenuItem.wav")
        self.stepConcrete = self.audioBufferLoader.load(path + "stepConcrete.wav")
        self.stepMetal = self.audioBufferLoader.load(path + "stepMetal.wav")
        self.switchTorch = self.audioBufferLoader.load(path + "switchTorch.wav")


def makeAudioBufferCollection(resolver):
    return AudioBufferCollection(resolver.resolve(AudioBufferLoader))
