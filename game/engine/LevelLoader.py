from game.levels.AuroraLevel import AuroraLevel
from game.levels.TestLevel import TestLevel


class LevelLoader:

    def load(self):
        level = AuroraLevel()
        level.validate()

        return level


def makeLevelLoader(resolver):
    return LevelLoader()
