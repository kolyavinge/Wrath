from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.engine.bsp.SplitBorderBuilder import *
from game.engine.bsp.SplitLineBuilder import *
from game.engine.CameraUpdater import *
from game.engine.cm.PlayerWallCollisionProcessor import *
from game.engine.GameData import *
from game.engine.GameUpdater import *
from game.engine.LevelLoader import *
from game.engine.LevelManager import *
from game.engine.LevelSegmentContentAnalyzer import *
from game.engine.LevelSegmentVisibilityUpdater import *
from game.engine.PlayerController import *
from game.engine.PlayerInputManager import *
from game.engine.PlayerPositionUpdater import *
from game.input.InputManager import *


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(SplitBorderBuilder, makeSplitBorderBuilder)
        binder.bindSingleton(SplitLineBuilder, makeSplitLineBuilder)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
        binder.bindSingleton(PlayerWallCollisionProcessor, makePlayerWallCollisionProcessor)
        binder.bindSingleton(GameData, makeGameData)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelManager, makeLevelManager)
        binder.bindSingleton(LevelSegmentContentAnalyzer, makeLevelSegmentContentAnalyzer)
        binder.bindSingleton(LevelSegmentVisibilityUpdater, makeLevelSegmentVisibilityUpdater)
        binder.bindSingleton(PlayerController, makePlayerController)
        binder.bindSingleton(PlayerInputManager, makePlayerInputManager)
        binder.bindSingleton(PlayerPositionUpdater, makePlayerPositionUpdater)
        binder.bindSingleton(InputManager, makeInputManager)
