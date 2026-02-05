from game.audio.AudioPlayer import AudioPlayer
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.WeaponAudioSources import WeaponAudioSources


class WeaponVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
    ):
        self.sources = {}
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer

    def init(self, gameState, allSources):
        self.sources = {}
        for person in gameState.allPerson:
            self.sources[person] = WeaponAudioSources(person, self.audioSourceFactory)
        allSources.extend(self.sources.values())

    def vox(self, updateStatistic):
        for person, weapon in updateStatistic.firedWeapons:
            source = self.sources[person]
            self.audioPlayer.play(source.shots[type(weapon)])

        for person, weapon in updateStatistic.reloadedWeapons:
            source = self.sources[person]
            self.audioPlayer.play(source.reloads[type(weapon)])

        for person, weapon in updateStatistic.putDownWeapons:
            source = self.sources[person]
            self.audioPlayer.play(source.putdown[type(weapon)])

        for person, weapon in updateStatistic.raisedWeapons:
            source = self.sources[person]
            self.audioPlayer.play(source.raises[type(weapon)])
