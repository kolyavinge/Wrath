from game.anx.Events import Events
from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PowerupAudioSources import PowerupAudioSources


class PowerupVox:

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
        eventManager.attachToEvent(Events.powerupPickedUp, self.onPowerupPickedUp)

    def init(self, allSources):
        self.source = PowerupAudioSources(self.gameData.player, self.audioSourceFactory)
        allSources.append(self.source)

    def onPowerupPickedUp(self, args):
        person, powerup = args
        if person == self.gameData.player:
            self.audioPlayer.play(self.source.powerups[type(powerup)])


def makePowerupVox(resolver):
    return PowerupVox(
        resolver.resolve(GameData),
        resolver.resolve(AudioSourceFactory),
        resolver.resolve(AudioPlayer),
        resolver.resolve(EventManager),
    )
