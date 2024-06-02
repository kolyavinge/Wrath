from game.engine.level.BSPTreeBuilder import BSPTreeBuilder, makeBSPTreeBuilder
from game.engine.level.BSPTreeTraversal import BSPTreeTraversal, makeBSPTreeTraversal
from game.engine.level.LevelLoader import LevelLoader, makeLevelLoader
from game.engine.level.LevelSegmentAnalyzer import LevelSegmentAnalyzer, makeLevelSegmentAnalyzer
from game.engine.Camera import Camera, makeCamera
from game.engine.GameUpdater import GameUpdater, makeGameUpdater


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(Camera, makeCamera)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
        binder.bindSingleton(BSPTreeBuilder, makeBSPTreeBuilder)
        binder.bindSingleton(BSPTreeTraversal, makeBSPTreeTraversal)
        binder.bindSingleton(LevelLoader, makeLevelLoader)
        binder.bindSingleton(LevelSegmentAnalyzer, makeLevelSegmentAnalyzer)
