from game.audio.AudioSourceLoader import AudioSourceLoader
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class AudioSourceFactory:

    def __init__(self, audioSourceLoader, audioBufferCollection):
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

    def makeRifleShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleShot)

    def makeWeaponPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.weaponPickup)


def makeAudioSourceFactory(resolver):
    return AudioSourceFactory(resolver.resolve(AudioSourceLoader), resolver.resolve(AudioBufferCollection))
