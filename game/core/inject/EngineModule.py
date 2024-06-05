from game.engine.level.bsp.BSPTreeBuilder import BSPTreeBuilder, makeBSPTreeBuilder
from game.engine.level.bsp.BSPTreeTraversal import BSPTreeTraversal, makeBSPTreeTraversal
from game.engine.level.LevelLoader import LevelLoader, makeLevelLoader
from game.engine.level.LevelManager import LevelManager, makeLevelManager
from game.engine.level.LevelSegmentAnalyzer import LevelSegmentAnalyzer, makeLevelSegmentAnalyzer
from game.engine.Camera import Camera, makeCamera
from game.engine.LevelUpdater import LevelUpdater, makeLevelUpdater
from game.input.InputManager import InputManager, makeInputManager


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(Camera, makeCamera)
        binder.bindSingleton(LevelUpdater, makeLevelUpdater)
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelManager, makeLevelManager)
        binder.bindSingleton(LevelSegmentAnalyzer, makeLevelSegmentAnalyzer)
        binder.bindSingleton(InputManager, makeInputManager)
