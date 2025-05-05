from game.calc.SphereSegmentCalculator import *
from game.engine.ai.AttackState import *
from game.engine.ai.CollisionDetector import *
from game.engine.ai.EnemyAILogic import *
from game.engine.ai.FireLogic import *
from game.engine.ai.HealthSearchState import *
from game.engine.ai.MovingLogic import *
from game.engine.ai.ObstacleAvoidanceLogic import *
from game.engine.ai.PatrollingState import *
from game.engine.ai.WeaponSearchState import *
from game.engine.AIDataInitializer import *
from game.engine.AimStateSwitcher import *
from game.engine.BackgroundVisibilityDetector import *
from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.BulletHoleFactory import *
from game.engine.BulletPositionUpdater import *
from game.engine.BulletTraceUpdater import *
from game.engine.BulletUpdater import *
from game.engine.CameraUpdater import *
from game.engine.cm.BulletCollisionDetector import *
from game.engine.cm.BulletCollisionProcessor import *
from game.engine.cm.PersonCollisionDetector import *
from game.engine.cm.PersonCollisionProcessor import *
from game.engine.cm.PersonWallCollisionDetector import *
from game.engine.cm.PersonWallCollisionProcessor import *
from game.engine.cm.PlaneCollisionDetector import *
from game.engine.cm.PowerupCollisionDetector import *
from game.engine.cm.PowerupCollisionProcessor import *
from game.engine.cm.WallCollisionDetector import *
from game.engine.EnemyLevelSegmentsUpdater import *
from game.engine.GameData import *
from game.engine.GameUpdater import *
from game.engine.LevelLoader import *
from game.engine.LevelManager import *
from game.engine.LevelSegmentItemFinder import *
from game.engine.LevelSegmentJoinLineAnalyzer import *
from game.engine.LevelSegmentLightAnalyzer import *
from game.engine.LevelSegmentVisibilityUpdater import *
from game.engine.LevelValidator import *
from game.engine.PersonDoStepLogic import *
from game.engine.PersonInitializer import *
from game.engine.PersonLevelSegmentsUpdater import *
from game.engine.PersonMovingTimeCalculator import *
from game.engine.PersonPositionUpdater import *
from game.engine.PersonTurnLogic import *
from game.engine.PersonVelocityCalculator import *
from game.engine.PersonWeaponPositionUpdater import *
from game.engine.PersonZUpdater import *
from game.engine.PlayerInputManager import *
from game.engine.PlayerLevelSegmentsUpdater import *
from game.engine.PlayerMovingSwingLogic import *
from game.engine.PlayerWeaponPositionSwingLogic import *
from game.engine.PowerupPositionGenerator import *
from game.engine.PowerupUpdater import *
from game.engine.TorchUpdater import *
from game.engine.WeaponDelayUpdater import *
from game.engine.WeaponFeedbackLogic import *
from game.engine.WeaponFireLogic import *
from game.engine.WeaponFlashUpdater import *
from game.engine.WeaponSelector import *
from game.input.InputManager import *


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(SphereSegmentCalculator, makeSphereSegmentCalculator)
        binder.bindSingleton(AttackState, makeAttackState)
        binder.bindSingleton(CollisionDetector, makeCollisionDetector)
        binder.bindSingleton(EnemyAILogic, makeEnemyAILogic)
        binder.bindSingleton(FireLogic, makeFireLogic)
        binder.bindSingleton(HealthSearchState, makeHealthSearchState)
        binder.bindSingleton(MovingLogic, makeMovingLogic)
        binder.bindSingleton(ObstacleAvoidanceLogic, makeObstacleAvoidanceLogic)
        binder.bindSingleton(PatrollingState, makePatrollingState)
        binder.bindSingleton(WeaponSearchState, makeWeaponSearchState)
        binder.bindSingleton(AIDataInitializer, makeAIDataInitializer)
        binder.bindSingleton(AimStateSwitcher, makeAimStateSwitcher)
        binder.bindSingleton(BackgroundVisibilityDetector, makeBackgroundVisibilityDetector)
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(BulletHoleFactory, makeBulletHoleFactory)
        binder.bindSingleton(BulletPositionUpdater, makeBulletPositionUpdater)
        binder.bindSingleton(BulletTraceUpdater, makeBulletTraceUpdater)
        binder.bindSingleton(BulletUpdater, makeBulletUpdater)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
        binder.bindSingleton(BulletCollisionDetector, makeBulletCollisionDetector)
        binder.bindSingleton(BulletCollisionProcessor, makeBulletCollisionProcessor)
        # binder.bindSingleton(ConstructionCollisionDetector, makeConstructionCollisionDetector)
        binder.bindSingleton(PersonCollisionDetector, makePersonCollisionDetector)
        binder.bindSingleton(PersonCollisionProcessor, makePersonCollisionProcessor)
        binder.bindSingleton(PersonWallCollisionDetector, makePersonWallCollisionDetector)
        binder.bindSingleton(PersonWallCollisionProcessor, makePersonWallCollisionProcessor)
        binder.bindSingleton(PlaneCollisionDetector, makePlaneCollisionDetector)
        binder.bindSingleton(PowerupCollisionDetector, makePowerupCollisionDetector)
        binder.bindSingleton(PowerupCollisionProcessor, makePowerupCollisionProcessor)
        binder.bindSingleton(WallCollisionDetector, makeWallCollisionDetector)
        binder.bindSingleton(EnemyLevelSegmentsUpdater, makeEnemyLevelSegmentsUpdater)
        binder.bindSingleton(GameData, makeGameData)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelManager, makeLevelManager)
        binder.bindSingleton(LevelSegmentItemFinder, makeLevelSegmentItemFinder)
        binder.bindSingleton(LevelSegmentJoinLineAnalyzer, makeLevelSegmentJoinLineAnalyzer)
        binder.bindSingleton(LevelSegmentLightAnalyzer, makeLevelSegmentLightAnalyzer)
        binder.bindSingleton(LevelSegmentVisibilityUpdater, makeLevelSegmentVisibilityUpdater)
        binder.bindSingleton(LevelValidator, makeLevelValidator)
        binder.bindSingleton(PersonDoStepLogic, makePersonDoStepLogic)
        binder.bindSingleton(PersonInitializer, makePersonInitializer)
        binder.bindSingleton(PersonLevelSegmentsUpdater, makePersonLevelSegmentsUpdater)
        binder.bindSingleton(PersonMovingTimeCalculator, makePersonMovingTimeCalculator)
        binder.bindSingleton(PersonPositionUpdater, makePersonPositionUpdater)
        binder.bindSingleton(PersonTurnLogic, makePersonTurnLogic)
        binder.bindSingleton(PersonVelocityCalculator, makePersonVelocityCalculator)
        binder.bindSingleton(PersonWeaponPositionUpdater, makePersonWeaponPositionUpdater)
        binder.bindSingleton(PersonZUpdater, makePersonZUpdater)
        binder.bindSingleton(PlayerInputManager, makePlayerInputManager)
        binder.bindSingleton(PlayerLevelSegmentsUpdater, makePlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMovingSwingLogic, makePlayerMovingSwingLogic)
        binder.bindSingleton(PlayerWeaponPositionSwingLogic, makePlayerWeaponPositionSwingLogic)
        binder.bindSingleton(PowerupPositionGenerator, makePowerupPositionGenerator)
        binder.bindSingleton(PowerupUpdater, makePowerupUpdater)
        binder.bindSingleton(TorchUpdater, makeTorchUpdater)
        binder.bindSingleton(WeaponDelayUpdater, makeWeaponDelayUpdater)
        binder.bindSingleton(WeaponFeedbackLogic, makeWeaponFeedbackLogic)
        binder.bindSingleton(WeaponFireLogic, makeWeaponFireLogic)
        binder.bindSingleton(WeaponFlashUpdater, makeWeaponFlashUpdater)
        binder.bindSingleton(WeaponSelector, makeWeaponSelector)
        binder.bindSingleton(InputManager, makeInputManager)
