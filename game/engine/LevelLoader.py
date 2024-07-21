from game.levels.Level1 import Level1
from game.levels.LevelLoop import LevelLoop


class LevelLoader:

    def loadFromFile(self):
        level = LevelLoop()
        level.validate()

        return level


def makeLevelLoader(resolver):
    return LevelLoader()
