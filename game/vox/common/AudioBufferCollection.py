from game.audio.AudioBufferLoader import AudioBufferLoader
from game.lib.Environment import Environment


class AudioBufferCollection:

    def __init__(self, audioBufferLoader):
        self.audioBufferLoader = audioBufferLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\audio\\"
        self.selectMenuItem = self.audioBufferLoader.load(path + "selectMenuItem.wav")


def makeAudioBufferCollection(resolver):
    return AudioBufferCollection(resolver.resolve(AudioBufferLoader))
