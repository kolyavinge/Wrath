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
        self.landing = self.audioBufferLoader.load(path + "landing.wav")
        self.pistolShot = self.audioBufferLoader.load(path + "pistolShot.wav")
        self.rifleShot = self.audioBufferLoader.load(path + "rifleShot.wav")
        self.launcherShot = self.audioBufferLoader.load(path + "launcherShot.wav")
        self.sniperShot = self.audioBufferLoader.load(path + "sniperShot.wav")
        self.weaponPickup = self.audioBufferLoader.load(path + "weaponPickup.wav")
        self.healthPickup = self.audioBufferLoader.load(path + "healthPickup.wav")
        self.vestPickup = self.audioBufferLoader.load(path + "vestPickup.wav")


def makeAudioBufferCollection(resolver):
    return AudioBufferCollection(resolver.resolve(AudioBufferLoader))
