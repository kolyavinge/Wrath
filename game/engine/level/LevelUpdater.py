from game.engine.level.LevelUpdater import LevelUpdater


class LevelUpdater:

    def __init__(self, levelManager):
        self.levelManager = levelManager

    def update(self):
        level = self.levelManager.currentLevel


def makeLevelUpdater(resolver):
    return LevelUpdater(resolver.resolve(LevelUpdater))
