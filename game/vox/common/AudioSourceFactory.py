from game.audio.AudioSourceLoader import AudioSourceLoader
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class AudioSourceFactory:

    def __init__(
        self,
        audioSourceLoader: AudioSourceLoader,
        audioBufferCollection: AudioBufferCollection,
    ):
        self.audioSourceLoader = audioSourceLoader
        self.audioBufferCollection = audioBufferCollection

    def makeSelectMenuItem(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.selectMenuItem)

    def makeStepConcrete(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.stepConcrete)

    def makeStepMetal(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.stepMetal)

    def makeSwitchTorch(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.switchTorch)

    def makeLanding(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.landing)

    def makePistolShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.pistolShot)

    def makeRifleShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleShot)

    def makePlasmaShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.plasmaShot)

    def makeLauncherShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.launcherShot)

    def makeRailgunShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.railgunShot)

    def makeSniperShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.sniperShot)

    def makeWeaponPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.weaponPickup)

    def makeHealthPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.healthPickup)

    def makeVestPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.vestPickup)


def makeAudioSourceFactory(resolver):
    return AudioSourceFactory(
        resolver.resolve(AudioSourceLoader),
        resolver.resolve(AudioBufferCollection),
    )
