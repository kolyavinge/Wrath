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
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    levelLoader: LevelLoader
    bspTreeBuilder: BSPTreeBuilder
    joinLineAnalyzer: LevelSegmentJoinLineAnalyzer
    lightAnalyzer: LevelSegmentLightAnalyzer
    levelValidator: LevelValidator
    personFloorUpdater: PersonFloorUpdater
    personInitializer: PersonInitializer
    aiDataInitializer: AIDataInitializer
    playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater
    enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater
    levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater
    cameraUpdater: CameraUpdater
    backgroundVisibilityDetector: BackgroundVisibilityUpdater
    personWeaponPositionUpdater: PersonWeaponPositionUpdater
    weaponFlashUpdater: WeaponFlashUpdater
    fragStatisticUpdater: FragStatisticUpdater
    enemyAIUpdater: EnemyAIUpdater

    def loadFirstLevel(self, gameState):
        level = self.levelLoader.load()
        gameState.level = level
        self.bspTreeBuilder.build(gameState.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(gameState.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, gameState.visibilityTree)
        self.levelValidator.validate(level, gameState.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, gameState.visibilityTree)
        self.personInitializer.init(gameState)
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personFloorUpdater.updateEnemyNextFloor(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.personFloorUpdater.commitEnemyNextFloor(gameState)
        self.aiDataInitializer.init(gameState)
        self.playerLevelSegmentsUpdater.update(gameState)
        self.enemyLevelSegmentsUpdater.update(gameState)
        self.cameraUpdater.update(gameState)
        self.levelSegmentVisibilityUpdater.update(gameState)
        self.backgroundVisibilityDetector.update(gameState)
        self.personWeaponPositionUpdater.update(gameState)
        self.fragStatisticUpdater.init(gameState)
        self.enemyAIUpdater.init(gameState)
