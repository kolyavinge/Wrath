from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.lib.AudioPlayer import AudioPlayer
from game.vox.sources.BulletAudioSources import BulletAudioSources


class BulletVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
    ):
        self.sources = {}
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer

    def init(self, allSources):
        self.source = BulletAudioSources(self.audioSourceFactory)
        allSources.append(self.source)

    def vox(self, updateStatistic):
        for person, weapon, bullet in updateStatistic.firedWeapons:
            if type(bullet) in self.source.bulletsPool:
                source = self.source.bulletsPool[type(bullet)].getAudioSource(bullet)
                source.setPosition(bullet.currentPosition)
                self.audioPlayer.play(source)

        for pool in self.source.bulletsPool.values():
            for source in pool.sources:
                if source.isPlaying():
                    bullet = source.object
                    if not bullet.isAlive:
                        self.audioPlayer.stop(source)

        for bullet in updateStatistic.bulletRicochets:
            if type(bullet) in self.source.bulletRicochetsPool:
                source = self.source.bulletRicochetsPool[type(bullet)].getAudioSource()
                source.setPosition(bullet.currentPosition)
                self.audioPlayer.play(source)
