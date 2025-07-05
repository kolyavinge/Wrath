from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.WeaponAudioSources import WeaponAudioSources


class WeaponVox:

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
        eventManager.attachToEvent(Events.weaponFired, self.onWeaponFired)
        eventManager.attachToEvent(Events.weaponReloaded, self.onWeaponReloaded)
        eventManager.attachToEvent(Events.weaponPutDown, self.onWeaponPutDown)
        eventManager.attachToEvent(Events.weaponRaised, self.onWeaponRaised)

    def init(self, allSources):
        self.sources = {}
        for person in self.gameData.allPerson:
            self.sources[person] = WeaponAudioSources(person, self.audioSourceFactory)
        allSources.extend(self.sources.values())

    def onWeaponFired(self, args):
        person, weapon = args
        source = self.sources[person]
        self.audioPlayer.play(source.shots[type(weapon)])

    def onWeaponReloaded(self, args):
        person, weapon = args
        source = self.sources[person]
        self.audioPlayer.play(source.reloads[type(weapon)])

    def onWeaponPutDown(self, args):
        person, weapon = args
        source = self.sources[person]
        self.audioPlayer.play(source.putdown[type(weapon)])

    def onWeaponRaised(self, args):
        person, weapon = args
        source = self.sources[person]
        self.audioPlayer.play(source.raises[type(weapon)])
