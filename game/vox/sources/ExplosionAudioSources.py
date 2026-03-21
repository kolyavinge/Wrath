from game.model.weapon.Launcher import LauncherExplosion
from game.model.weapon.Plasma import PlasmaExplosion
from game.model.weapon.Rifle import RifleGrenadeExplosion
from game.vox.lib.AudioSourcePool import AudioSourcePool


class ExplosionAudioSources:

    def __init__(self, audioSourceFactory):

        def makeRifleGrenadeExplosion():
            source = audioSourceFactory.makeRifleGrenadeExplosion()
            source.setGain(10)
            return source

        def makeLauncherExplosion():
            source = audioSourceFactory.makeLauncherExplosion()
            source.setGain(10)
            return source

        self.explosionsPool = {}
        self.explosionsPool[RifleGrenadeExplosion] = AudioSourcePool(makeRifleGrenadeExplosion)
        self.explosionsPool[PlasmaExplosion] = AudioSourcePool(audioSourceFactory.makePlasmaExplosion)
        self.explosionsPool[LauncherExplosion] = AudioSourcePool(makeLauncherExplosion)

    def updatePosition(self):
        pass

    def release(self):
        for pool in self.explosionsPool.values():
            pool.release()
