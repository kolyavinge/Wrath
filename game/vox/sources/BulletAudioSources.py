from game.model.weapon.Launcher import LauncherBullet
from game.model.weapon.Rifle import RifleGrenade
from game.vox.lib.AudioSourcePool import AudioSourcePool


class BulletAudioSources:

    def __init__(self, audioSourceFactory):

        def makeLauncherBullet():
            source = audioSourceFactory.makeLauncherBullet()
            source.setGain(10)
            source.setLooping()
            return source

        self.bulletsPool = {}
        self.bulletsPool[LauncherBullet] = AudioSourcePool(makeLauncherBullet)

        def makeGrenadeRicochet():
            source = audioSourceFactory.makeGrenadeRicochet()
            source.setGain(0.5)
            return source

        self.bulletRicochetsPool = {}
        self.bulletRicochetsPool[RifleGrenade] = AudioSourcePool(makeGrenadeRicochet)

    def updatePosition(self):
        for pool in self.bulletsPool.values():
            for source in pool.sources:
                bullet = source.object
                source.setPosition(bullet.currentPosition)

    def release(self):
        for pool in self.bulletsPool.values():
            pool.release()

        for pool in self.bulletRicochetsPool.values():
            pool.release()
