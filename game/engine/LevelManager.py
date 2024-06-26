from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentFloorAnalyzer import LevelSegmentFloorAnalyzer
from game.engine.LevelSegmentValidator import LevelSegmentValidator
from game.engine.LevelSegmentWallAnalyzer import LevelSegmentWallAnalyzer


class LevelManager:

    def __init__(self, gameData, levelLoader, bspTreeBuilder, segmentWallAnalyzer, segmentFloorAnalyzer, segmentValidator):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.segmentWallAnalyzer = segmentWallAnalyzer
        self.segmentFloorAnalyzer = segmentFloorAnalyzer
        self.segmentValidator = segmentValidator

    def loadFirstLevel(self):
        level = self.levelLoader.loadFromFile()
        self.gameData.level = level
        self.bspTreeBuilder.build(level)
        self.segmentWallAnalyzer.analyzeWalls(level)
        self.segmentFloorAnalyzer.analyzeFloors(level)
        self.segmentValidator.validate(level)


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData),
        resolver.resolve(LevelLoader),
        resolver.resolve(BSPTreeBuilder),
        resolver.resolve(LevelSegmentWallAnalyzer),
        resolver.resolve(LevelSegmentFloorAnalyzer),
        resolver.resolve(LevelSegmentValidator),
    )
