from game.calc.RayOrientationLogic import *
from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.CameraScopeChecker import *
from game.engine.CameraUpdater import *
from game.engine.cm.BulletCollisionDetector import *
from game.engine.cm.BulletCollisionUpdater import *
from game.engine.cm.ConstructionCollisionDetector import *
from game.engine.cm.ExplosionCollisionDetector import *
from game.engine.cm.ExplosionCollisionUpdater import *
from game.engine.cm.PersonCeilingCollisionDetector import *
from game.engine.cm.PersonCeilingCollisionUpdater import *
from game.engine.cm.PersonCollisionDetector import *
from game.engine.cm.PersonCollisionUpdater import *
from game.engine.cm.PersonWallCollisionDetector import *
from game.engine.cm.PersonWallCollisionUpdater import *
from game.engine.cm.PlaneCollisionDetector import *
from game.engine.cm.PowerupCollisionDetector import *
from game.engine.cm.PowerupCollisionUpdater import *
from game.engine.cm.SphereCollisionDetector import *
from game.engine.cm.VoidCollisionDetector import *
from game.engine.DashboardUpdater import *
from game.engine.GameData import *
from game.engine.GameUpdater import *
from game.engine.level.BackgroundVisibilityUpdater import *
from game.engine.level.LevelLoader import *
from game.engine.level.LevelManager import *
from game.engine.level.LevelSegmentItemFinder import *
from game.engine.level.LevelSegmentJoinLineAnalyzer import *
from game.engine.level.LevelSegmentLightAnalyzer import *
from game.engine.level.LevelValidator import *
from game.engine.level.PersonInitializer import *
from game.engine.person.AIDataInitializer import *
from game.engine.person.AimStateSwitcher import *
from game.engine.person.CowboyEasterEggUpdater import *
from game.engine.person.EnemyLevelSegmentsUpdater import *
from game.engine.person.EnemyLifeBarUpdater import *
from game.engine.person.EnemyVisibilityUpdater import *
from game.engine.person.FragStatisticUpdater import *
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonBreathUpdater import *
from game.engine.person.PersonDamageLogic import *
from game.engine.person.PersonFloorUpdater import *
from game.engine.person.PersonJumpUpdater import *
from game.engine.person.PersonLevelSegmentsUpdater import *
from game.engine.person.PersonLifeCycleUpdater import *
from game.engine.person.PersonMovingTimeUpdater import *
from game.engine.person.PersonPositionUpdater import *
from game.engine.person.PersonRespawnUpdater import *
from game.engine.person.PersonSelectedWeaponPositionUpdater import *
from game.engine.person.PersonStepUpdater import *
from game.engine.person.PersonTurnLogic import *
from game.engine.person.PersonTurnUpdater import *
from game.engine.person.PersonUpdater import *
from game.engine.person.PersonVelocityUpdater import *
from game.engine.person.PersonWeaponPositionUpdater import *
from game.engine.person.PersonZUpdater import *
from game.engine.person.PlayerBloodStainUpdater import *
from game.engine.person.PlayerLevelSegmentsUpdater import *
from game.engine.person.PlayerMovingSwingUpdater import *
from game.engine.person.PlayerWeaponSwingUpdater import *
from game.engine.person.TorchUpdater import *
from game.engine.powerup.PowerupPositionGenerator import *
from game.engine.powerup.PowerupProcessor import *
from game.engine.powerup.PowerupUpdater import *
from game.engine.powerup.PowerupValidator import *
from game.engine.weapon.alt.LauncherAltFireLogic import *
from game.engine.weapon.alt.PistolAltFireLogic import *
from game.engine.weapon.alt.RailgunAltFireLogic import *
from game.engine.weapon.alt.SniperAltFireLogic import *
from game.engine.weapon.BulletHoleFactory import *
from game.engine.weapon.BulletLogic import *
from game.engine.weapon.BulletPositionUpdater import *
from game.engine.weapon.BulletTraceUpdater import *
from game.engine.weapon.BulletUpdater import *
from game.engine.weapon.ExplosionLogic import *
from game.engine.weapon.ExplosionUpdater import *
from game.engine.weapon.NonStandardBulletMovingUpdater import *
from game.engine.weapon.PlasmaBulletMovingLogic import *
from game.engine.weapon.SelectWeaponRequestListener import *
from game.engine.weapon.SniperAimFloatingUpdater import *
from game.engine.weapon.WeaponAltFireUpdater import *
from game.engine.weapon.WeaponDelayUpdater import *
from game.engine.weapon.WeaponFeedbackLogic import *
from game.engine.weapon.WeaponFireLogic import *
from game.engine.weapon.WeaponFireUpdater import *
from game.engine.weapon.WeaponFlashUpdater import *
from game.engine.weapon.WeaponSelector import *
from game.input.InputManager import *
from game.input.PlayerInputManager import *


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(RayOrientationLogic)
        binder.bindSingleton(EnemyAIUpdater)
        binder.bindSingleton(BSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal)
        binder.bindSingleton(CameraScopeChecker)
        binder.bindSingleton(CameraUpdater)
        binder.bindSingleton(BulletCollisionDetector)
        binder.bindSingleton(BulletCollisionUpdater)
        binder.bindSingleton(ConstructionCollisionDetector)
        binder.bindSingleton(ExplosionCollisionDetector)
        binder.bindSingleton(ExplosionCollisionUpdater)
        binder.bindSingleton(PersonCeilingCollisionDetector)
        binder.bindSingleton(PersonCeilingCollisionUpdater)
        binder.bindSingleton(PersonCollisionDetector)
        binder.bindSingleton(PersonCollisionUpdater)
        binder.bindSingleton(PersonWallCollisionDetector)
        binder.bindSingleton(PersonWallCollisionUpdater)
        binder.bindSingleton(PlaneCollisionDetector)
        binder.bindSingleton(PowerupCollisionDetector)
        binder.bindSingleton(PowerupCollisionUpdater)
        binder.bindSingleton(SphereCollisionDetector)
        binder.bindSingleton(VoidCollisionDetector)
        binder.bindSingleton(DashboardUpdater)
        binder.bindSingleton(GameData)
        binder.bindSingleton(GameUpdater, resolveByFields=True)
        binder.bindSingleton(BackgroundVisibilityUpdater)
        binder.bindSingleton(LevelLoader)
        binder.bindSingleton(LevelManager, resolveByFields=True)
        binder.bindSingleton(LevelSegmentItemFinder)
        binder.bindSingleton(LevelSegmentJoinLineAnalyzer)
        binder.bindSingleton(LevelSegmentLightAnalyzer)
        binder.bindSingleton(LevelValidator)
        binder.bindSingleton(PersonInitializer)
        binder.bindSingleton(AIDataInitializer)
        binder.bindSingleton(AimStateSwitcher)
        binder.bindSingleton(CowboyEasterEggUpdater)
        binder.bindSingleton(EnemyLevelSegmentsUpdater)
        binder.bindSingleton(EnemyLifeBarUpdater)
        binder.bindSingleton(EnemyVisibilityUpdater)
        binder.bindSingleton(FragStatisticUpdater)
        binder.bindSingleton(LevelSegmentVisibilityUpdater)
        binder.bindSingleton(PersonBreathUpdater)
        binder.bindSingleton(PersonDamageLogic)
        binder.bindSingleton(PersonFloorUpdater)
        binder.bindSingleton(PersonJumpUpdater)
        binder.bindSingleton(PersonLevelSegmentsUpdater)
        binder.bindSingleton(PersonLifeCycleUpdater)
        binder.bindSingleton(PersonMovingTimeUpdater)
        binder.bindSingleton(PersonPositionUpdater)
        binder.bindSingleton(PersonRespawnUpdater)
        binder.bindSingleton(PersonSelectedWeaponPositionUpdater)
        binder.bindSingleton(PersonStepUpdater)
        binder.bindSingleton(PersonTurnLogic)
        binder.bindSingleton(PersonTurnUpdater)
        binder.bindSingleton(PersonUpdater)
        binder.bindSingleton(PersonVelocityUpdater)
        binder.bindSingleton(PersonWeaponPositionUpdater)
        binder.bindSingleton(PersonZUpdater)
        binder.bindSingleton(PlayerBloodStainUpdater)
        binder.bindSingleton(PlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMovingSwingUpdater)
        binder.bindSingleton(PlayerWeaponSwingUpdater)
        binder.bindSingleton(TorchUpdater)
        binder.bindSingleton(PowerupPositionGenerator)
        binder.bindSingleton(PowerupProcessor)
        binder.bindSingleton(PowerupUpdater)
        binder.bindSingleton(PowerupValidator)
        binder.bindSingleton(LauncherAltFireLogic)
        binder.bindSingleton(PistolAltFireLogic)
        binder.bindSingleton(RailgunAltFireLogic)
        binder.bindSingleton(SniperAltFireLogic)
        binder.bindSingleton(BulletHoleFactory)
        binder.bindSingleton(BulletLogic)
        binder.bindSingleton(BulletPositionUpdater)
        binder.bindSingleton(BulletTraceUpdater)
        binder.bindSingleton(BulletUpdater)
        binder.bindSingleton(ExplosionLogic)
        binder.bindSingleton(ExplosionUpdater)
        binder.bindSingleton(NonStandardBulletMovingUpdater)
        binder.bindSingleton(PlasmaBulletMovingLogic)
        binder.bindSingleton(SelectWeaponRequestListener)
        binder.bindSingleton(SniperAimFloatingUpdater)
        binder.bindSingleton(WeaponAltFireUpdater)
        binder.bindSingleton(WeaponDelayUpdater)
        binder.bindSingleton(WeaponFeedbackLogic)
        binder.bindSingleton(WeaponFireLogic)
        binder.bindSingleton(WeaponFireUpdater)
        binder.bindSingleton(WeaponFlashUpdater)
        binder.bindSingleton(WeaponSelector)
        binder.bindSingleton(InputManager)
        binder.bindSingleton(PlayerInputManager)
