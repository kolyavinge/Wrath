from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.bsp.SplitBorderBuilder import *
from game.engine.bsp.SplitLineBuilder import *
from game.engine.CameraUpdater import *
from game.engine.cm.PlayerWallCollisionProcessor import *
from game.engine.EmptyLevelSegmentCleaner import *
from game.engine.GameData import *
from game.engine.GameUpdater import *
from game.engine.LevelLoader import *
from game.engine.LevelManager import *
from game.engine.LevelSegmentFloorAnalyzer import *
from game.engine.LevelSegmentItemFinder import *
from game.engine.LevelSegmentVisibilityUpdater import *
from game.engine.LevelSegmentWallAnalyzer import *
from game.engine.LevelValidator import *
from game.engine.PlayerInputManager import *
from game.engine.PlayerLevelSegmentsUpdater import *
from game.engine.PlayerMoveLogic import *
from game.engine.PlayerPositionUpdater import *
from game.engine.PlayerTurnLogic import *
from game.engine.PlayerZUpdater import *
from game.input.InputManager import *


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(SplitLineBuilder, makeSplitLineBuilder)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
        binder.bindSingleton(PlayerWallCollisionProcessor, makePlayerWallCollisionProcessor)
        binder.bindSingleton(EmptyLevelSegmentCleaner, makeEmptyLevelSegmentCleaner)
        binder.bindSingleton(GameData, makeGameData)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelManager, makeLevelManager)
        binder.bindSingleton(LevelSegmentFloorAnalyzer, makeLevelSegmentFloorAnalyzer)
        binder.bindSingleton(LevelSegmentItemFinder, makeLevelSegmentItemFinder)
        binder.bindSingleton(LevelSegmentVisibilityUpdater, makeLevelSegmentVisibilityUpdater)
        binder.bindSingleton(LevelSegmentWallAnalyzer, makeLevelSegmentWallAnalyzer)
        binder.bindSingleton(LevelValidator, makeLevelValidator)
        binder.bindSingleton(PlayerInputManager, makePlayerInputManager)
        binder.bindSingleton(PlayerLevelSegmentsUpdater, makePlayerLevelSegmentsUpdater)
        binder.bindSingleton(PlayerMoveLogic, makePlayerMoveLogic)
        binder.bindSingleton(PlayerPositionUpdater, makePlayerPositionUpdater)
        binder.bindSingleton(PlayerTurnLogic, makePlayerTurnLogic)
        binder.bindSingleton(PlayerZUpdater, makePlayerZUpdater)
        binder.bindSingleton(InputManager, makeInputManager)
