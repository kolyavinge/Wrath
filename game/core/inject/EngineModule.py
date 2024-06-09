from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder, makeBSPTreeBuilder
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal, makeBSPTreeTraversal
from game.engine.CameraUpdater import CameraUpdater, makeCameraUpdater
from game.engine.GameData import GameData, makeGameData
from game.engine.GameUpdater import GameUpdater, makeGameUpdater
from game.engine.LevelLoader import LevelLoader, makeLevelLoader
from game.engine.LevelManager import LevelManager, makeLevelManager
from game.engine.LevelSegmentContentAnalyzer import LevelSegmentContentAnalyzer, makeLevelSegmentContentAnalyzer
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater, makeLevelSegmentVisibilityUpdater
from game.engine.PlayerController import PlayerController, makePlayerController
from game.engine.PlayerInputManager import PlayerInputManager, makePlayerInputManager
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater, makePlayerPositionUpdater
from game.input.InputManager import InputManager, makeInputManager


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(CameraUpdater, makeCameraUpdater)
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
