from game.engine.level.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.level.LevelLoader import LevelLoader
from game.engine.level.LevelSegmentAnalyzer import LevelSegmentAnalyzer


class LevelManager:

    def __init__(self, levelLoader, bspTreeBuilder, levelSegmentAnalyzer):
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.levelSegmentAnalyzer = levelSegmentAnalyzer

    def load(self):
        self.currentLevel = self.levelLoader.loadLevel()
        self.bspTreeBuilder.build(self.currentLevel)
        self.levelSegmentAnalyzer.analyze(self.currentLevel)


def makeLevelManager(resolver):
    return LevelManager(resolver.resolve(LevelLoader), resolver.resolve(BSPTreeBuilder), resolver.resolve(LevelSegmentAnalyzer))
