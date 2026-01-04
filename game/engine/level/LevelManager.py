from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.CameraUpdater import CameraUpdater
from game.engine.GameState import GameState
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.level.LevelLoader import LevelLoader
from game.engine.level.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.level.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.level.LevelValidator import LevelValidator
from game.engine.level.PersonInitializer import PersonInitializer
from game.engine.person.AIDataInitializer import AIDataInitializer
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class LevelManager:

    gameData: GameState
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

    def loadFirstLevel(self):
        level = self.levelLoader.load()
        self.gameData.level = level
        self.bspTreeBuilder.build(self.gameData.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(self.gameData.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, self.gameData.visibilityTree)
        self.levelValidator.validate(level, self.gameData.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, self.gameData.visibilityTree)
        self.personInitializer.init()
        self.personFloorUpdater.updateNextFloor()
        self.personFloorUpdater.commitNextFloor()
        self.aiDataInitializer.init()
        self.playerLevelSegmentsUpdater.update()
        self.enemyLevelSegmentsUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()
        self.backgroundVisibilityDetector.update()
        self.personWeaponPositionUpdater.update()
        self.weaponFlashUpdater.init()
        self.fragStatisticUpdater.init()
        self.enemyAIUpdater.init()
