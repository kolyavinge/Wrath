from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentContentAnalyzer import LevelSegmentContentAnalyzer
from game.engine.GameData import GameData


class LevelManager:

    def __init__(self, gameData, levelLoader, bspTreeBuilder, segmentContentAnalyzer):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.segmentContentAnalyzer = segmentContentAnalyzer

    def loadFirstLevel(self):
        level = self.levelLoader.loadFromFile()
        self.bspTreeBuilder.build(level)
        self.segmentContentAnalyzer.analyze(level)
        self.gameData.level = level


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData), resolver.resolve(LevelLoader), resolver.resolve(BSPTreeBuilder), resolver.resolve(LevelSegmentContentAnalyzer)
    )
