from game.audio.AudioBufferLoader import AudioBufferLoader
from game.lib.Environment import Environment


class AudioBufferCollection:

    def __init__(self, audioBufferLoader: AudioBufferLoader):
        self.audioBufferLoader = audioBufferLoader

    def init(self):
        audioFolder = f"{Environment.programRootPath}\\res\\audio\\"

        def loadWav(wavFileName):
            return self.audioBufferLoader.load(f"{audioFolder}{wavFileName}.wav")

        self.selectMenuItem = loadWav("selectMenuItem")
        self.stepConcrete = loadWav("stepConcrete")
        self.stepMetal = loadWav("stepMetal")
        self.switchTorch = loadWav("switchTorch")
        self.jumping = loadWav("jumping")
        self.landing = loadWav("landing")
        self.pistolRaise = loadWav("pistolRaise")
        self.rifleRaise = loadWav("rifleRaise")
        self.plasmaRaise = loadWav("plasmaRaise")
        self.launcherRaise = loadWav("launcherRaise")
        self.railgunRaise = loadWav("railgunRaise")
        self.sniperRaise = loadWav("sniperRaise")
        self.pistolShot = loadWav("pistolShot")
        self.rifleShot = loadWav("rifleShot")
        self.rifleGrenade = loadWav("rifleGrenade")
        self.plasmaShot = loadWav("plasmaShot")
        self.launcherShot = loadWav("launcherShot")
        self.railgunShot = loadWav("railgunShot")
        self.sniperShot = loadWav("sniperShot")
        self.sniperReload = loadWav("sniperReload")
        self.weaponPutdown = loadWav("weaponPutdown")
        self.weaponPickup = loadWav("weaponPickup")
        self.healthPickup = loadWav("healthPickup")
        self.vestPickup = loadWav("vestPickup")
