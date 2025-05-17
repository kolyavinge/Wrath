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
from game.engine.powerup.PowerupValidator import *
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
        binder.bindSingleton(SphereSegmentCalculator)
        binder.bindSingleton(BurstFireLogic)
        binder.bindSingleton(CollisionDetector)
        binder.bindSingleton(FireLogic)
        binder.bindSingleton(MovingLogic)
        binder.bindSingleton(ObstacleAvoidanceLogic)
        binder.bindSingleton(EnemyAIUpdater)
        binder.bindSingleton(AttackStateHandler)
        binder.bindSingleton(HealthSearchStateHandler)
        binder.bindSingleton(PatrollingStateHandler)
        binder.bindSingleton(StateHandlerCollection)
        binder.bindSingleton(WeaponSearchStateHandler)
        binder.bindSingleton(BSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal)
        binder.bindSingleton(CameraUpdater)
        binder.bindSingleton(BulletCollisionDetector)
        binder.bindSingleton(BulletCollisionUpdater)
        binder.bindSingleton(PersonCollisionDetector)
        binder.bindSingleton(PersonCollisionUpdater)
        binder.bindSingleton(PersonWallCollisionDetector)
        binder.bindSingleton(PersonWallCollisionUpdater)
        binder.bindSingleton(PlaneCollisionDetector)
        binder.bindSingleton(PowerupCollisionDetector)
        binder.bindSingleton(PowerupCollisionUpdater)
        binder.bindSingleton(WallCollisionDetector)
        binder.bindSingleton(GameData)
        binder.bindSingleton(GameUpdater, resolveByFields=True)
        binder.bindSingleton(LevelLoader)
        binder.bindSingleton(LevelManager)
        binder.bindSingleton(LevelSegmentItemFinder)
        binder.bindSingleton(LevelSegmentJoinLineAnalyzer)
        binder.bindSingleton(LevelSegmentLightAnalyzer)
        binder.bindSingleton(LevelValidator)
        binder.bindSingleton(PersonInitializer)
        binder.bindSingleton(AIDataInitializer)
        binder.bindSingleton(AimStateSwitcher)
        binder.bindSingleton(BackgroundVisibilityUpdater)
        binder.bindSingleton(EnemyLevelSegmentsUpdater)
        binder.bindSingleton(LevelSegmentVisibilityUpdater)
        binder.bindSingleton(PersonDamageLogic)
        binder.bindSingleton(PersonLevelSegmentsUpdater)
        binder.bindSingleton(PersonMovingTimeUpdater)
        binder.bindSingleton(PersonPositionUpdater)
        binder.bindSingleton(PersonStepUpdater)
        binder.bindSingleton(PersonTurnLogic)
        binder.bindSingleton(PersonTurnUpdater)
        binder.bindSingleton(PersonUpdater)
        binder.bindSingleton(PersonVelocityUpdater)
        binder.bindSingleton(PersonWeaponPositionUpdater)
        binder.bindSingleton(PersonZUpdater)
        binder.bindSingleton(PlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMovingSwingUpdater)
        binder.bindSingleton(PlayerWeaponSwingUpdater)
        binder.bindSingleton(TorchUpdater)
        binder.bindSingleton(PowerupPositionGenerator)
        binder.bindSingleton(PowerupUpdater)
        binder.bindSingleton(PowerupValidator)
        binder.bindSingleton(BulletHoleFactory)
        binder.bindSingleton(BulletPositionUpdater)
        binder.bindSingleton(BulletTraceUpdater)
        binder.bindSingleton(BulletUpdater)
        binder.bindSingleton(NonStandardBulletMovingUpdater)
        binder.bindSingleton(PlasmaBulletMovingLogic)
        binder.bindSingleton(WeaponDelayUpdater)
        binder.bindSingleton(WeaponFeedbackLogic)
        binder.bindSingleton(WeaponFireUpdater)
        binder.bindSingleton(WeaponFlashUpdater)
        binder.bindSingleton(WeaponSelector)
        binder.bindSingleton(InputManager)
        binder.bindSingleton(PlayerInputManager)
