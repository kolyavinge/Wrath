from game.engine.level.BSPTreeBuilder import BSPTreeBuilder
from game.engine.level.LevelSegmentAnalyzer import LevelSegmentAnalyzer


class LevelLoader:

    def __init__(self, bspTreeBuilder, levelSegmentAnalyzer):
        self.bspTreeBuilder = bspTreeBuilder
        self.levelSegmentAnalyzer = levelSegmentAnalyzer

    def load(self):
        level = None
        self.bspTreeBuilder.build(level)
        self.levelSegmentAnalyzer.analyze(level)


def makeLevelLoader(resolver):
    return LevelLoader(resolver.resolve(BSPTreeBuilder), resolver.resolve(LevelSegmentAnalyzer))
