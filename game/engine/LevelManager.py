from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.bsp.BSPTreeBuilder2 import BSPTreeBuilder2
from game.engine.bsp.SplitLineBuilder import SplitLineBuilder
from game.engine.CameraUpdater import CameraUpdater
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentCeilingAnalyzer import LevelSegmentCeilingAnalyzer
from game.engine.LevelSegmentFloorAnalyzer import LevelSegmentFloorAnalyzer
from game.engine.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.LevelSegmentWallAnalyzer import LevelSegmentWallAnalyzer
from game.engine.LevelValidator import LevelValidator
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic


class LevelManager:

    def __init__(
        self,
        gameData,
        levelLoader,
        bspTreeBuilder,
        bspTreeBuilder2,
        splitLineBuilder,
        segmentWallAnalyzer,
        segmentFloorAnalyzer,
        segmentCeilingAnalyzer,
        joinLineCeilingAnalyzer,
        levelValidator,
        playerTurnLogic,
        playerLevelSegmentsUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
    ):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.bspTreeBuilder2 = bspTreeBuilder2
        self.splitLineBuilder = splitLineBuilder
        self.segmentWallAnalyzer = segmentWallAnalyzer
        self.segmentFloorAnalyzer = segmentFloorAnalyzer
        self.segmentCeilingAnalyzer = segmentCeilingAnalyzer
        self.joinLineCeilingAnalyzer = joinLineCeilingAnalyzer
        self.levelValidator = levelValidator
        self.playerTurnLogic = playerTurnLogic
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def loadFirstLevel(self):
        level = self.levelLoader.load()
        self.gameData.level = level
        self.bspTreeBuilder2.build(level.collisionTree, level, level.getCollisionSplitPlanes())
        self.bspTreeBuilder2.build(level.visibilityTree, level, level.getVisibilitySplitPlanes())
        # self.segmentWallAnalyzer.analyzeWalls(level, level.collisionTree)
        # self.segmentFloorAnalyzer.analyzeFloors(level, level.collisionTree)
        # self.segmentCeilingAnalyzer.analyzeCeilings(level, level.collisionTree)
        # self.segmentWallAnalyzer.analyzeWalls(level, level.visibilityTree)
        # self.segmentFloorAnalyzer.analyzeFloors(level, level.visibilityTree)
        # self.segmentCeilingAnalyzer.analyzeCeilings(level, level.visibilityTree)
        self.joinLineCeilingAnalyzer.analyzeJoinLines(level, level.visibilityTree)
        self.levelValidator.validate(level)
        self.playerTurnLogic.orientByFrontNormal(level.playerFrontNormal)
        self.gameData.player.moveNextPositionTo(level.playerPosition)
        self.gameData.player.commitNextPosition()
        self.playerLevelSegmentsUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData),
        resolver.resolve(LevelLoader),
        resolver.resolve(BSPTreeBuilder),
        resolver.resolve(BSPTreeBuilder2),
        resolver.resolve(SplitLineBuilder),
        resolver.resolve(LevelSegmentWallAnalyzer),
        resolver.resolve(LevelSegmentFloorAnalyzer),
        resolver.resolve(LevelSegmentCeilingAnalyzer),
        resolver.resolve(LevelSegmentJoinLineAnalyzer),
        resolver.resolve(LevelValidator),
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
    )
