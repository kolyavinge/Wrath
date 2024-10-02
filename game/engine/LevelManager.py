from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.CameraUpdater import CameraUpdater
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.LevelValidator import LevelValidator
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic


class LevelManager:

    def __init__(
        self,
        gameData,
        levelLoader,
        bspTreeBuilder,
        joinLineAnalyzer,
        lightAnalyzer,
        levelValidator,
        playerTurnLogic,
        playerLevelSegmentsUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
    ):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.joinLineAnalyzer = joinLineAnalyzer
        self.lightAnalyzer = lightAnalyzer
        self.levelValidator = levelValidator
        self.playerTurnLogic = playerTurnLogic
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def loadFirstLevel(self):
        level = self.levelLoader.load()
        self.gameData.level = level
        self.bspTreeBuilder.build(level.collisionTree, level, level.getCollisionSplitPlanes())
        self.bspTreeBuilder.build(level.visibilityTree, level, level.getVisibilitySplitPlanes())
        self.joinLineAnalyzer.analyzeJoinLines(level, level.visibilityTree)
        self.levelValidator.validate(level)
        self.lightAnalyzer.analyzeLights(level.visibilityTree)
        self.playerTurnLogic.orientByFrontNormal(level.playerFrontNormal)
        self.gameData.player.moveNextPositionTo(level.playerPosition)
        self.gameData.player.commitNextPosition()
        self.playerLevelSegmentsUpdater.update()
        self.cameraUpdater.updatePosition()
        self.levelSegmentVisibilityUpdater.update()


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData),
        resolver.resolve(LevelLoader),
        resolver.resolve(BSPTreeBuilder),
        resolver.resolve(LevelSegmentJoinLineAnalyzer),
        resolver.resolve(LevelSegmentLightAnalyzer),
        resolver.resolve(LevelValidator),
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
    )
