from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.level.LevelLoader import LevelLoader
from game.engine.level.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.level.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.level.LevelValidator import LevelValidator
from game.engine.level.PersonInitializer import PersonInitializer
from game.engine.person.AIDataInitializer import AIDataInitializer
from game.engine.person.CameraUpdater import CameraUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    def __init__(
        self,
        levelLoader: LevelLoader,
        bspTreeBuilder: BSPTreeBuilder,
        joinLineAnalyzer: LevelSegmentJoinLineAnalyzer,
        lightAnalyzer: LevelSegmentLightAnalyzer,
        levelValidator: LevelValidator,
        personInitializer: PersonInitializer,
        aiDataInitializer: AIDataInitializer,
        levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater,
        cameraUpdater: CameraUpdater,
        backgroundVisibilityDetector: BackgroundVisibilityUpdater,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        weaponFlashUpdater: WeaponFlashUpdater,
        fragStatisticUpdater: FragStatisticUpdater,
        enemyAIUpdater: EnemyAIUpdater,
    ):
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.joinLineAnalyzer = joinLineAnalyzer
        self.lightAnalyzer = lightAnalyzer
        self.levelValidator = levelValidator
        self.personInitializer = personInitializer
        self.aiDataInitializer = aiDataInitializer
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.backgroundVisibilityDetector = backgroundVisibilityDetector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.weaponFlashUpdater = weaponFlashUpdater
        self.fragStatisticUpdater = fragStatisticUpdater
        self.enemyAIUpdater = enemyAIUpdater

    def loadFirstLevel(self, gameState):
        level = self.levelLoader.load()
        gameState.level = level
        self.bspTreeBuilder.build(gameState.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(gameState.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, gameState.visibilityTree)
        self.levelValidator.validate(level, gameState.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, gameState.visibilityTree)
        self.personInitializer.init(gameState)
        self.aiDataInitializer.init(gameState)
        self.cameraUpdater.update(gameState)
        self.levelSegmentVisibilityUpdater.update(gameState)
        self.backgroundVisibilityDetector.update(gameState)
        self.personWeaponPositionUpdater.update(gameState)
        self.fragStatisticUpdater.init(gameState)
        self.enemyAIUpdater.init(gameState)
