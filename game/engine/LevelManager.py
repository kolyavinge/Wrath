from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentWallAnalyzer import LevelSegmentWallAnalyzer


class LevelManager:

    def __init__(self, gameData, levelLoader, bspTreeBuilder, segmentWallAnalyzer):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.segmentWallAnalyzer = segmentWallAnalyzer

    def loadFirstLevel(self):
        level = self.levelLoader.loadFromFile()
        self.bspTreeBuilder.build(level)
        self.segmentWallAnalyzer.analyzeWalls(level)
        self.gameData.level = level


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData), resolver.resolve(LevelLoader), resolver.resolve(BSPTreeBuilder), resolver.resolve(LevelSegmentWallAnalyzer)
    )
