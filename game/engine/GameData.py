from game.model.Person import Person
from game.model.Camera import Camera


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = []
        self.player = Person()
        self.camera = Camera()
        self.playerLevelSegment = None


def makeGameData(resolver):
    return GameData()
