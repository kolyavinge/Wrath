from game.vox.common.AudioBufferCollection import AudioBufferCollection
from game.vox.lib.AudioSourceLoader import AudioSourceLoader


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

    def makeJumping(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.jumping)

    def makeLanding(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.landing)

    def makePistolRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.pistolRaise)

    def makeRifleRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleRaise)

    def makePlasmaRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.plasmaRaise)

    def makeLauncherRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.launcherRaise)

    def makeRailgunRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.railgunRaise)

    def makeSniperRaise(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.sniperRaise)

    def makePistolShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.pistolShot)

    def makeRifleShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleShot)

    def makeRifleGrenadeShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleGrenadeShot)

    def makeRifleGrenadeExplosion(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.rifleGrenadeExplosion)

    def makePlasmaShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.plasmaShot)

    def makePlasmaExplosion(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.plasmaExplosion)

    def makeLauncherShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.launcherShot)

    def makeLauncherBullet(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.launcherBullet)

    def makeLauncherExplosion(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.launcherExplosion)

    def makeRailgunShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.railgunShot)

    def makeSniperShot(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.sniperShot)

    def makeSniperReload(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.sniperReload)

    def makeGrenadeRicochet(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.grenadeRicochet)

    def makeWeaponPutdown(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.weaponPutdown)

    def makeWeaponPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.weaponPickup)

    def makeHealthPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.healthPickup)

    def makeVestPickup(self):
        return self.audioSourceLoader.load(self.audioBufferCollection.vestPickup)
