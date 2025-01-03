from game.calc.SphereSegmentCalculator import *
from game.engine.BackgroundVisibilityDetector import *
from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.BulletHoleFactory import *
from game.engine.BulletMoveLogic import *
from game.engine.BulletTraceUpdater import *
from game.engine.BulletUpdater import *
from game.engine.CameraUpdater import *
from game.engine.cm.BulletCollisionDetector import *
from game.engine.cm.BulletCollisionProcessor import *
from game.engine.cm.ConstructionCollisionDetector import *
from game.engine.cm.PlaneCollisionDetector import *
from game.engine.cm.PlayerWallCollisionDetector import *
from game.engine.cm.PlayerWallCollisionProcessor import *
from game.engine.cm.PowerupCollisionDetector import *
from game.engine.cm.PowerupCollisionProcessor import *
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
from game.engine.PlayerInputManager import *
from game.engine.PlayerLevelSegmentsUpdater import *
from game.engine.PlayerMoveLogic import *
from game.engine.PlayerMovingSwingLogic import *
from game.engine.PlayerMovingTimeCalculator import *
from game.engine.PlayerPositionUpdater import *
from game.engine.PlayerTurnLogic import *
from game.engine.PlayerVelocityCalculator import *
from game.engine.PlayerWeaponPositionSwingLogic import *
from game.engine.PlayerWeaponPositionUpdater import *
from game.engine.PlayerZUpdater import *
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
        binder.bindSingleton(BackgroundVisibilityDetector, makeBackgroundVisibilityDetector)
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(BulletHoleFactory, makeBulletHoleFactory)
        binder.bindSingleton(BulletMoveLogic, makeBulletMoveLogic)
        binder.bindSingleton(BulletTraceUpdater, makeBulletTraceUpdater)
        binder.bindSingleton(BulletUpdater, makeBulletUpdater)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
        binder.bindSingleton(BulletCollisionDetector, makeBulletCollisionDetector)
        binder.bindSingleton(BulletCollisionProcessor, makeBulletCollisionProcessor)
        binder.bindSingleton(ConstructionCollisionDetector, makeConstructionCollisionDetector)
        binder.bindSingleton(PlaneCollisionDetector, makePlaneCollisionDetector)
        binder.bindSingleton(PlayerWallCollisionDetector, makePlayerWallCollisionDetector)
        binder.bindSingleton(PlayerWallCollisionProcessor, makePlayerWallCollisionProcessor)
        binder.bindSingleton(PowerupCollisionDetector, makePowerupCollisionDetector)
        binder.bindSingleton(PowerupCollisionProcessor, makePowerupCollisionProcessor)
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
        binder.bindSingleton(PlayerInputManager, makePlayerInputManager)
        binder.bindSingleton(PlayerLevelSegmentsUpdater, makePlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMoveLogic, makePlayerMoveLogic)
        binder.bindSingleton(PlayerMovingSwingLogic, makePlayerMovingSwingLogic)
        binder.bindSingleton(PlayerMovingTimeCalculator, makePlayerMovingTimeCalculator)
        binder.bindSingleton(PlayerPositionUpdater, makePlayerPositionUpdater)
        binder.bindSingleton(PlayerTurnLogic, makePlayerTurnLogic)
        binder.bindSingleton(PlayerVelocityCalculator, makePlayerVelocityCalculator)
        binder.bindSingleton(PlayerWeaponPositionSwingLogic, makePlayerWeaponPositionSwingLogic)
        binder.bindSingleton(PlayerWeaponPositionUpdater, makePlayerWeaponPositionUpdater)
        binder.bindSingleton(PlayerZUpdater, makePlayerZUpdater)
        binder.bindSingleton(PowerupPositionGenerator, makePowerupPositionGenerator)
        binder.bindSingleton(PowerupUpdater, makePowerupUpdater)
        binder.bindSingleton(TorchUpdater, makeTorchUpdater)
        binder.bindSingleton(WeaponDelayUpdater, makeWeaponDelayUpdater)
        binder.bindSingleton(WeaponFeedbackLogic, makeWeaponFeedbackLogic)
        binder.bindSingleton(WeaponFireLogic, makeWeaponFireLogic)
        binder.bindSingleton(WeaponFlashUpdater, makeWeaponFlashUpdater)
        binder.bindSingleton(WeaponSelector, makeWeaponSelector)
        binder.bindSingleton(InputManager, makeInputManager)
