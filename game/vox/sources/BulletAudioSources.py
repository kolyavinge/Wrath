from game.model.weapon.Rifle import RifleGrenade
from game.vox.lib.AudioSourcePool import AudioSourcePool


class BulletAudioSources:

    def __init__(self, audioSourceFactory):

        def makeGrenadeRicochet():
            source = audioSourceFactory.makeGrenadeRicochet()
            source.setGain(0.5)
            return source

        self.bulletRicochetsPool = {}
        self.bulletRicochetsPool[RifleGrenade] = AudioSourcePool(makeGrenadeRicochet)

    def updatePosition(self):
        pass

    def release(self):
        for pool in self.bulletRicochetsPool.values():
            pool.release()
