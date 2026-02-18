from game.audio.AudioPlayer import AudioPlayer
from game.model.Material import MaterialKind
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PersonAudioSources import PersonAudioSources


class PersonVox:

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
        self.allSources = allSources
        self.addPerson(gameState.player)

    def addPerson(self, person):
        source = PersonAudioSources(person, self.audioSourceFactory)
        self.sources[person] = source
        self.allSources.append(source)

    def vox(self, updateStatistic):
        for person in updateStatistic.stepedPerson:
            source = self.sources[person]
            if person.currentFloor.material.kind == MaterialKind.concrete:
                self.audioPlayer.play(source.stepConcrete)
            elif person.currentFloor.material.kind == MaterialKind.metal:
                self.audioPlayer.play(source.stepMetal)

        for person in updateStatistic.jumpedPerson:
            source = self.sources[person]
            self.audioPlayer.play(source.jumping)

        for person in updateStatistic.landedPerson:
            source = self.sources[person]
            self.audioPlayer.play(source.landing)
