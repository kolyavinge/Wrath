from game.audio.AudioSourcePool import AudioSourcePool
from game.model.weapon.Launcher import LauncherExplosion
from game.model.weapon.Plasma import PlasmaExplosion
from game.model.weapon.Rifle import RifleGrenadeExplosion


class ExplosionAudioSources:

    def __init__(self, audioSourceFactory):
        self.explosionsPool = {}
        self.explosionsPool[RifleGrenadeExplosion] = AudioSourcePool(audioSourceFactory.makeRifleGrenadeExplosion)
        self.explosionsPool[PlasmaExplosion] = AudioSourcePool(audioSourceFactory.makePlasmaExplosion)
        self.explosionsPool[LauncherExplosion] = AudioSourcePool(audioSourceFactory.makeLauncherExplosion)

    def updatePosition(self):
        pass

    def release(self):
        for pool in self.explosionsPool.values():
            pool.release()
