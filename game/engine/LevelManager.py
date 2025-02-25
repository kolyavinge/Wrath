from game.engine.BackgroundVisibilityDetector import BackgroundVisibilityDetector
from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.CameraUpdater import CameraUpdater
from game.engine.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.GameData import GameData
from game.engine.LevelLoader import LevelLoader
from game.engine.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.LevelValidator import LevelValidator
from game.engine.PersonInitializer import PersonInitializer
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerWeaponPositionUpdater import PlayerWeaponPositionUpdater
from game.engine.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    def __init__(
        self,
        gameData,
        levelLoader,
        bspTreeBuilder,
        joinLineAnalyzer,
        lightAnalyzer,
        levelValidator,
        personInitializer,
        playerLevelSegmentsUpdater,
        enemyLevelSegmentsUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        backgroundVisibilityDetector,
        playerWeaponPositionUpdater,
        weaponFlashUpdater,
    ):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.joinLineAnalyzer = joinLineAnalyzer
        self.lightAnalyzer = lightAnalyzer
        self.levelValidator = levelValidator
        self.personInitializer = personInitializer
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.enemyLevelSegmentsUpdater = enemyLevelSegmentsUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.backgroundVisibilityDetector = backgroundVisibilityDetector
        self.playerWeaponPositionUpdater = playerWeaponPositionUpdater
        self.weaponFlashUpdater = weaponFlashUpdater

    def loadFirstLevel(self):
        level = self.levelLoader.load()
        self.gameData.level = level
        self.bspTreeBuilder.build(self.gameData.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(self.gameData.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, self.gameData.visibilityTree)
        self.levelValidator.validate(level, self.gameData.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, self.gameData.visibilityTree)
        self.personInitializer.init()
        self.playerLevelSegmentsUpdater.update()
        self.enemyLevelSegmentsUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()
        self.backgroundVisibilityDetector.update()
        self.playerWeaponPositionUpdater.update()
        self.weaponFlashUpdater.init()


def makeLevelManager(resolver):
    return LevelManager(
        resolver.resolve(GameData),
        resolver.resolve(LevelLoader),
        resolver.resolve(BSPTreeBuilder),
        resolver.resolve(LevelSegmentJoinLineAnalyzer),
        resolver.resolve(LevelSegmentLightAnalyzer),
        resolver.resolve(LevelValidator),
        resolver.resolve(PersonInitializer),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(EnemyLevelSegmentsUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(BackgroundVisibilityDetector),
        resolver.resolve(PlayerWeaponPositionUpdater),
        resolver.resolve(WeaponFlashUpdater),
    )
