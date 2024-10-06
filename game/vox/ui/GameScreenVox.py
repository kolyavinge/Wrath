from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.vox.common.PersonVox import PersonVox


class GameScreenVox:

    def __init__(self, gameData, audioPlayer, personVox):
        self.allSources = []
        self.gameData = gameData
        self.audioPlayer = audioPlayer
        self.personVox = personVox

    def init(self):
        for source in self.allSources:
            source.release()

        self.allSources = []
        self.personVox.init(self.allSources)

    def update(self):
        self.audioPlayer.setListenerPosition(self.gameData.player.currentCenterPoint)
        for source in self.allSources:
            source.updatePosition()


def makeGameScreenVox(resolver):
    return GameScreenVox(resolver.resolve(GameData), resolver.resolve(AudioPlayer), resolver.resolve(PersonVox))
