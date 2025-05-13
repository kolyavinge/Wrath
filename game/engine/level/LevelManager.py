from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.CameraUpdater import CameraUpdater
from game.engine.GameData import GameData
from game.engine.level.LevelLoader import LevelLoader
from game.engine.level.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.level.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.level.LevelValidator import LevelValidator
from game.engine.level.PersonInitializer import PersonInitializer
from game.engine.person.AIDataInitializer import AIDataInitializer
from game.engine.person.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    def __init__(
        self,
        gameData: GameData,
        levelLoader: LevelLoader,
        bspTreeBuilder: BSPTreeBuilder,
        joinLineAnalyzer: LevelSegmentJoinLineAnalyzer,
        lightAnalyzer: LevelSegmentLightAnalyzer,
        levelValidator: LevelValidator,
        personInitializer: PersonInitializer,
        aiDataInitializer: AIDataInitializer,
        playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater,
        enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater,
        levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater,
        cameraUpdater: CameraUpdater,
        backgroundVisibilityDetector: BackgroundVisibilityUpdater,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        weaponFlashUpdater: WeaponFlashUpdater,
    ):
        self.gameData = gameData
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.joinLineAnalyzer = joinLineAnalyzer
        self.lightAnalyzer = lightAnalyzer
        self.levelValidator = levelValidator
        self.personInitializer = personInitializer
        self.aiDataInitializer = aiDataInitializer
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.enemyLevelSegmentsUpdater = enemyLevelSegmentsUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.backgroundVisibilityDetector = backgroundVisibilityDetector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
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
        self.aiDataInitializer.init()
        self.playerLevelSegmentsUpdater.update()
        self.enemyLevelSegmentsUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()
        self.backgroundVisibilityDetector.update()
        self.personWeaponPositionUpdater.update()
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
        resolver.resolve(AIDataInitializer),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(EnemyLevelSegmentsUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(BackgroundVisibilityUpdater),
        resolver.resolve(PersonWeaponPositionUpdater),
        resolver.resolve(WeaponFlashUpdater),
    )
