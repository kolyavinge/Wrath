from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.WeaponAudioSources import WeaponAudioSources


class WeaponVox:

    def __init__(self, gameData, audioSourceFactory, audioPlayer, eventManager):
        self.sources = {}
        self.gameData = gameData
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.weaponFired, self.onWeaponFired)

    def init(self, allSources):
        self.sources = {}
        self.sources[self.gameData.player] = WeaponAudioSources(self.gameData.player, self.audioSourceFactory)
        # other enemies
        allSources.extend(self.sources.values())

    def onWeaponFired(self, args):
        person, weapon = args
        source = self.sources[person]
        self.audioPlayer.play(source.weapons[type(weapon)])


def makeWeaponVox(resolver):
    return WeaponVox(
        resolver.resolve(GameData),
        resolver.resolve(AudioSourceFactory),
        resolver.resolve(AudioPlayer),
        resolver.resolve(EventManager),
    )
