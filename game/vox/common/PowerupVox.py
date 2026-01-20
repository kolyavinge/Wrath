from game.audio.AudioPlayer import AudioPlayer
from game.lib.EventManager import EventManager, Events
from game.vox.common.AudioSourceFactory import AudioSourceFactory
from game.vox.sources.PowerupAudioSources import PowerupAudioSources


class PowerupVox:

    def __init__(
        self,
        audioSourceFactory: AudioSourceFactory,
        audioPlayer: AudioPlayer,
        eventManager: EventManager,
    ):
        self.sources = {}
        self.audioSourceFactory = audioSourceFactory
        self.audioPlayer = audioPlayer
        eventManager.attachToEvent(Events.powerupPickedUp, self.onPowerupPickedUp)

    def init(self, gameState, allSources):
        self.source = PowerupAudioSources(gameState.player, self.audioSourceFactory)
        allSources.append(self.source)

    def onPowerupPickedUp(self, args):
        person, powerup = args
        if person == self.gameState.player:
            self.audioPlayer.play(self.source.powerups[type(powerup)])
