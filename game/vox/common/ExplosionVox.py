from game.audio.AudioPlayer import AudioPlayer
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.ExplosionAudioSources import ExplosionAudioSources


class ExplosionVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
    ):
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer

    def init(self, allSources):
        self.source = ExplosionAudioSources(self.audioSourceFactory)
        allSources.append(self.source)

    def vox(self, updateStatistic):
        for explosion in updateStatistic.newExplosions:
            source = self.source.explosionsPool[type(explosion)].getAudioSource()
            source.setPosition(explosion.position)
            source.setGain(10.0)
            self.audioPlayer.play(source)
