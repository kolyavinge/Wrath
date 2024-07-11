from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.bsp.SplitLineBuilder import SplitLineBuilder
from game.engine.EmptyLevelSegmentCleaner import EmptyLevelSegmentCleaner
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentCeilingAnalyzer import LevelSegmentCeilingAnalyzer
from game.engine.LevelSegmentFloorAnalyzer import LevelSegmentFloorAnalyzer
from game.engine.LevelSegmentWallAnalyzer import LevelSegmentWallAnalyzer
from game.engine.LevelValidator import LevelValidator
from game.engine.PlayerTurnLogic import PlayerTurnLogic


class LevelManager:

    def __init__(
        self,
        gameData,
        levelLoader,
        bspTreeBuilder,
        splitLineBuilder,
        segmentWallAnalyzer,
        segmentFloorAnalyzer,
        segmentCeilingAnalyzer,
        segmentCleaner,
        levelValidator,
        playerTurnLogic,
    ):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.splitLineBuilder = splitLineBuilder
        self.segmentWallAnalyzer = segmentWallAnalyzer
        self.segmentFloorAnalyzer = segmentFloorAnalyzer
        self.segmentCeilingAnalyzer = segmentCeilingAnalyzer
        self.segmentCleaner = segmentCleaner
        self.levelValidator = levelValidator
        self.playerTurnLogic = playerTurnLogic

    def loadFirstLevel(self):
        level = self.levelLoader.loadFromFile()
        self.gameData.level = level
        self.bspTreeBuilder.build(level.collisionTree, self.splitLineBuilder.getForCollisions(level))
        self.bspTreeBuilder.build(level.visibilityTree, self.splitLineBuilder.getForVisibility(level))
        self.segmentWallAnalyzer.analyzeWalls(level, level.collisionTree)
        self.segmentFloorAnalyzer.analyzeFloors(level, level.collisionTree)
        self.segmentCeilingAnalyzer.analyzeCeilings(level, level.collisionTree)
        self.segmentWallAnalyzer.analyzeWalls(level, level.visibilityTree)
        self.segmentFloorAnalyzer.analyzeFloors(level, level.visibilityTree)
        self.segmentCeilingAnalyzer.analyzeCeilings(level, level.visibilityTree)
        self.segmentCleaner.clean(level.collisionTree)
        self.segmentCleaner.clean(level.visibilityTree)
        self.levelValidator.validate(level)
        self.playerTurnLogic.orientByFrontNormal(level.playerFrontNormal)
        self.gameData.player.moveNextPositionTo(level.playerPosition)
        self.gameData.player.commitNextPosition()


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData),
        resolver.resolve(LevelLoader),
        resolver.resolve(BSPTreeBuilder),
        resolver.resolve(SplitLineBuilder),
        resolver.resolve(LevelSegmentWallAnalyzer),
        resolver.resolve(LevelSegmentFloorAnalyzer),
        resolver.resolve(LevelSegmentCeilingAnalyzer),
        resolver.resolve(EmptyLevelSegmentCleaner),
        resolver.resolve(LevelValidator),
        resolver.resolve(PlayerTurnLogic),
    )
