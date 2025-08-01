from game.audio.AudioBufferLoader import AudioBufferLoader
from game.lib.Environment import Environment


class AudioBufferCollection:

    def __init__(self, audioBufferLoader: AudioBufferLoader):
        self.audioBufferLoader = audioBufferLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\audio\\"
        self.selectMenuItem = self.audioBufferLoader.load(path + "selectMenuItem.wav")
        self.stepConcrete = self.audioBufferLoader.load(path + "stepConcrete.wav")
        self.stepMetal = self.audioBufferLoader.load(path + "stepMetal.wav")
        self.switchTorch = self.audioBufferLoader.load(path + "switchTorch.wav")
        self.jumping = self.audioBufferLoader.load(path + "jumping.wav")
        self.landing = self.audioBufferLoader.load(path + "landing.wav")
        self.pistolRaise = self.audioBufferLoader.load(path + "pistolRaise.wav")
        self.rifleRaise = self.audioBufferLoader.load(path + "rifleRaise.wav")
        self.plasmaRaise = self.audioBufferLoader.load(path + "plasmaRaise.wav")
        self.launcherRaise = self.audioBufferLoader.load(path + "launcherRaise.wav")
        self.railgunRaise = self.audioBufferLoader.load(path + "railgunRaise.wav")
        self.sniperRaise = self.audioBufferLoader.load(path + "sniperRaise.wav")
        self.pistolShot = self.audioBufferLoader.load(path + "pistolShot.wav")
        self.rifleShot = self.audioBufferLoader.load(path + "rifleShot.wav")
        self.plasmaShot = self.audioBufferLoader.load(path + "plasmaShot.wav")
        self.launcherShot = self.audioBufferLoader.load(path + "launcherShot.wav")
        self.railgunShot = self.audioBufferLoader.load(path + "railgunShot.wav")
        self.sniperShot = self.audioBufferLoader.load(path + "sniperShot.wav")
        self.sniperReload = self.audioBufferLoader.load(path + "sniperReload.wav")
        self.weaponPutdown = self.audioBufferLoader.load(path + "weaponPutdown.wav")
        self.weaponPickup = self.audioBufferLoader.load(path + "weaponPickup.wav")
        self.healthPickup = self.audioBufferLoader.load(path + "healthPickup.wav")
        self.vestPickup = self.audioBufferLoader.load(path + "vestPickup.wav")
