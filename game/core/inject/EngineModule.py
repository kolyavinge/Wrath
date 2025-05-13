from game.calc.SphereSegmentCalculator import *
from game.engine.ai.common.BurstFireLogic import *
from game.engine.ai.common.CollisionDetector import *
from game.engine.ai.common.FireLogic import *
from game.engine.ai.common.MovingLogic import *
from game.engine.ai.common.ObstacleAvoidanceLogic import *
from game.engine.ai.EnemyAIUpdater import *
from game.engine.ai.state.AttackStateHandler import *
from game.engine.ai.state.HealthSearchStateHandler import *
from game.engine.ai.state.PatrollingStateHandler import *
from game.engine.ai.state.StateHandlerCollection import *
from game.engine.ai.state.WeaponSearchStateHandler import *
from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.CameraUpdater import *
from game.engine.cm.BulletCollisionDetector import *
from game.engine.cm.BulletCollisionUpdater import *
from game.engine.cm.PersonCollisionDetector import *
from game.engine.cm.PersonCollisionUpdater import *
from game.engine.cm.PersonWallCollisionDetector import *
from game.engine.cm.PersonWallCollisionUpdater import *
from game.engine.cm.PlaneCollisionDetector import *
from game.engine.cm.PowerupCollisionDetector import *
from game.engine.cm.PowerupCollisionUpdater import *
from game.engine.cm.WallCollisionDetector import *
from game.engine.GameData import *
from game.engine.GameUpdater import *
from game.engine.level.LevelLoader import *
from game.engine.level.LevelManager import *
from game.engine.level.LevelSegmentItemFinder import *
from game.engine.level.LevelSegmentJoinLineAnalyzer import *
from game.engine.level.LevelSegmentLightAnalyzer import *
from game.engine.level.LevelValidator import *
from game.engine.level.PersonInitializer import *
from game.engine.person.AIDataInitializer import *
from game.engine.person.AimStateSwitcher import *
from game.engine.person.BackgroundVisibilityUpdater import *
from game.engine.person.EnemyLevelSegmentsUpdater import *
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonDamageLogic import *
from game.engine.person.PersonLevelSegmentsUpdater import *
from game.engine.person.PersonMovingTimeUpdater import *
from game.engine.person.PersonPositionUpdater import *
from game.engine.person.PersonStepUpdater import *
from game.engine.person.PersonTurnLogic import *
from game.engine.person.PersonTurnUpdater import *
from game.engine.person.PersonUpdater import *
from game.engine.person.PersonVelocityUpdater import *
from game.engine.person.PersonWeaponPositionUpdater import *
from game.engine.person.PersonZUpdater import *
from game.engine.person.PlayerLevelSegmentsUpdater import *
from game.engine.person.PlayerMovingSwingUpdater import *
from game.engine.person.PlayerWeaponSwingUpdater import *
from game.engine.person.TorchUpdater import *
from game.engine.powerup.PowerupPositionGenerator import *
from game.engine.powerup.PowerupUpdater import *
from game.engine.weapon.BulletHoleFactory import *
from game.engine.weapon.BulletPositionUpdater import *
from game.engine.weapon.BulletTraceUpdater import *
from game.engine.weapon.BulletUpdater import *
from game.engine.weapon.NonStandardBulletMovingUpdater import *
from game.engine.weapon.PlasmaBulletMovingLogic import *
from game.engine.weapon.WeaponDelayUpdater import *
from game.engine.weapon.WeaponFeedbackLogic import *
from game.engine.weapon.WeaponFireUpdater import *
from game.engine.weapon.WeaponFlashUpdater import *
from game.engine.weapon.WeaponSelector import *
from game.input.InputManager import *
from game.input.PlayerInputManager import *


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(SphereSegmentCalculator, makeSphereSegmentCalculator)
        binder.bindSingleton(BurstFireLogic, makeBurstFireLogic)
        binder.bindSingleton(CollisionDetector, makeCollisionDetector)
        binder.bindSingleton(FireLogic, makeFireLogic)
        binder.bindSingleton(MovingLogic, makeMovingLogic)
        binder.bindSingleton(ObstacleAvoidanceLogic, makeObstacleAvoidanceLogic)
        binder.bindSingleton(EnemyAIUpdater, makeEnemyAIUpdater)
        binder.bindSingleton(AttackStateHandler, makeAttackStateHandler)
        binder.bindSingleton(HealthSearchStateHandler, makeHealthSearchStateHandler)
        binder.bindSingleton(PatrollingStateHandler, makePatrollingStateHandler)
        binder.bindSingleton(StateHandlerCollection, makeStateHandlerCollection)
        binder.bindSingleton(WeaponSearchStateHandler, makeWeaponSearchStateHandler)
        binder.bindSingleton(BackgroundVisibilityUpdater, makeBackgroundVisibilityUpdater)
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(BulletPositionUpdater, makeBulletPositionUpdater)
        binder.bindSingleton(BulletTraceUpdater, makeBulletTraceUpdater)
        binder.bindSingleton(BulletUpdater, makeBulletUpdater)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
        binder.bindSingleton(BulletCollisionDetector, makeBulletCollisionDetector)
        binder.bindSingleton(BulletCollisionUpdater, makeBulletCollisionUpdater)
        # binder.bindSingleton(ConstructionCollisionDetector, makeConstructionCollisionDetector)
        binder.bindSingleton(PersonCollisionDetector, makePersonCollisionDetector)
        binder.bindSingleton(PersonCollisionUpdater, makePersonCollisionUpdater)
        binder.bindSingleton(PersonWallCollisionDetector, makePersonWallCollisionDetector)
        binder.bindSingleton(PersonWallCollisionUpdater, makePersonWallCollisionUpdater)
        binder.bindSingleton(PlaneCollisionDetector, makePlaneCollisionDetector)
        binder.bindSingleton(PowerupCollisionDetector, makePowerupCollisionDetector)
        binder.bindSingleton(PowerupCollisionUpdater, makePowerupCollisionUpdater)
        binder.bindSingleton(WallCollisionDetector, makeWallCollisionDetector)
        binder.bindSingleton(EnemyLevelSegmentsUpdater, makeEnemyLevelSegmentsUpdater)
        binder.bindSingleton(GameData, makeGameData)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
        binder.bindSingleton(LevelManager, makeLevelManager)
        binder.bindSingleton(LevelSegmentVisibilityUpdater, makeLevelSegmentVisibilityUpdater)
        binder.bindSingleton(AIDataInitializer, makeAIDataInitializer)
        binder.bindSingleton(AimStateSwitcher, makeAimStateSwitcher)
        binder.bindSingleton(BulletHoleFactory, makeBulletHoleFactory)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelSegmentItemFinder, makeLevelSegmentItemFinder)
        binder.bindSingleton(LevelSegmentJoinLineAnalyzer, makeLevelSegmentJoinLineAnalyzer)
        binder.bindSingleton(LevelSegmentLightAnalyzer, makeLevelSegmentLightAnalyzer)
        binder.bindSingleton(LevelValidator, makeLevelValidator)
        binder.bindSingleton(PersonDamageLogic, makePersonDamageLogic)
        binder.bindSingleton(PersonInitializer, makePersonInitializer)
        binder.bindSingleton(PersonTurnLogic, makePersonTurnLogic)
        binder.bindSingleton(PlasmaBulletMovingLogic, makePlasmaBulletMovingLogic)
        binder.bindSingleton(PowerupPositionGenerator, makePowerupPositionGenerator)
        binder.bindSingleton(WeaponFeedbackLogic, makeWeaponFeedbackLogic)
        binder.bindSingleton(WeaponSelector, makeWeaponSelector)
        binder.bindSingleton(NonStandardBulletMovingUpdater, makeNonStandardBulletMovingUpdater)
        binder.bindSingleton(PersonLevelSegmentsUpdater, makePersonLevelSegmentsUpdater)
        binder.bindSingleton(PersonMovingTimeUpdater, makePersonMovingTimeUpdater)
        binder.bindSingleton(PersonPositionUpdater, makePersonPositionUpdater)
        binder.bindSingleton(PersonStepUpdater, makePersonStepUpdater)
        binder.bindSingleton(PersonTurnUpdater, makePersonTurnUpdater)
        binder.bindSingleton(PersonUpdater, makePersonUpdater)
        binder.bindSingleton(PersonVelocityUpdater, makePersonVelocityUpdater)
        binder.bindSingleton(PersonWeaponPositionUpdater, makePersonWeaponPositionUpdater)
        binder.bindSingleton(PersonZUpdater, makePersonZUpdater)
        binder.bindSingleton(PlayerLevelSegmentsUpdater, makePlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMovingSwingUpdater, makePlayerMovingSwingUpdater)
        binder.bindSingleton(PlayerWeaponSwingUpdater, makePlayerWeaponSwingUpdater)
        binder.bindSingleton(PowerupUpdater, makePowerupUpdater)
        binder.bindSingleton(TorchUpdater, makeTorchUpdater)
        binder.bindSingleton(WeaponDelayUpdater, makeWeaponDelayUpdater)
        binder.bindSingleton(WeaponFireUpdater, makeWeaponFireUpdater)
        binder.bindSingleton(WeaponFlashUpdater, makeWeaponFlashUpdater)
        binder.bindSingleton(InputManager, makeInputManager)
        binder.bindSingleton(PlayerInputManager, makePlayerInputManager)
