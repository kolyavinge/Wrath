from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.Material import MaterialKind
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PersonAudioSources import PersonAudioSources


class PersonVox:

    def __init__(
        self,
        gameData: GameData,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
        eventManager: EventManager,
    ):
        self.sources = {}
        self.gameData = gameData
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.personStepDone, self.onPersonStepDone)
        eventManager.attachToEvent(Events.personLanded, self.onPersonLanded)

    def init(self, allSources):
        self.sources = {}
        for person in self.gameData.allPerson:
            self.sources[person] = PersonAudioSources(person, self.audioSourceFactory)
        allSources.extend(self.sources.values())

    def onPersonStepDone(self, person):
        source = self.sources[person]
        if person.currentFloor.material.kind == MaterialKind.concrete:
            self.audioPlayer.play(source.stepConcrete)
        elif person.currentFloor.material.kind == MaterialKind.metal:
            self.audioPlayer.play(source.stepMetal)

    def onPersonLanded(self, person):
        self.onPersonStepDone(person)
        source = self.sources[person]
        self.audioPlayer.play(source.landing)
