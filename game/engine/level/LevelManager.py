from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.GameState import GameState
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
from game.engine.person.TorchUpdater import TorchUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    gameState: GameState
    levelLoader: LevelLoader
    bspTreeBuilder: BSPTreeBuilder
    joinLineAnalyzer: LevelSegmentJoinLineAnalyzer
    lightAnalyzer: LevelSegmentLightAnalyzer
    levelValidator: LevelValidator
    personFloorUpdater: PersonFloorUpdater
    personInitializer: PersonInitializer
    torchUpdater: TorchUpdater
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

    def loadFirstLevel(self):
        level = self.levelLoader.load()
        self.gameState.level = level
        self.bspTreeBuilder.build(self.gameState.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(self.gameState.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, self.gameState.visibilityTree)
        self.levelValidator.validate(level, self.gameState.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, self.gameState.visibilityTree)
        self.personInitializer.init()
        self.torchUpdater.init(self.gameState)
        self.personFloorUpdater.updatePlayerNextFloor(self.gameState)
        self.personFloorUpdater.updateEnemyNextFloor(self.gameState)
        self.personFloorUpdater.commitPlayerNextFloor(self.gameState)
        self.personFloorUpdater.commitEnemyNextFloor(self.gameState)
        self.aiDataInitializer.init()
        self.playerLevelSegmentsUpdater.update(self.gameState)
        self.enemyLevelSegmentsUpdater.update(self.gameState)
        self.cameraUpdater.update(self.gameState)
        self.levelSegmentVisibilityUpdater.update(self.gameState)
        self.backgroundVisibilityDetector.update(self.gameState)
        self.personWeaponPositionUpdater.update(self.gameState)
        self.fragStatisticUpdater.init(self.gameState)
        self.enemyAIUpdater.init(self.gameState)
