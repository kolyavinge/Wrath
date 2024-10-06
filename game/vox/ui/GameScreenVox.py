from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData
from game.vox.common.PersonVox import PersonVox


class GameScreenVox:

    def __init__(self, gameData, audioPlayer, personVox):
        self.gameData = gameData
        self.audioPlayer = audioPlayer
        self.personVox = personVox

    def init(self):
        self.personVox.init()

    def update(self):
        self.audioPlayer.setListenerPosition(self.gameData.player.currentCenterPoint)
        self.personVox.update()


def makeGameScreenVox(resolver):
    return GameScreenVox(resolver.resolve(GameData), resolver.resolve(AudioPlayer), resolver.resolve(PersonVox))
