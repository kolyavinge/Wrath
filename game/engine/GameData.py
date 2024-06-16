from game.model.Camera import Camera
from game.model.Person import Person


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = []
        self.player = Person()
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
