from game.audio.AudioPlayer import AudioPlayer
from game.engine.GameData import GameData


class GameScreenVox:

    def __init__(self, gameData, audioPlayer):
        self.gameData = gameData
        self.audioPlayer = audioPlayer

    def update(self):
        self.audioPlayer.setListenerPosition(self.gameData.player.currentCenterPoint)


def makeGameScreenVox(resolver):
    return GameScreenVox(resolver.resolve(GameData), resolver.resolve(AudioPlayer))
