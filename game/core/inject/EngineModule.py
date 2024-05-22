from game.engine.Camera import Camera, makeCamera
from game.engine.GameUpdater import GameUpdater, makeGameUpdater


class EngineModule:

    def init(self, binder):
        binder.bindSingleton(Camera, makeCamera)
        binder.bindSingleton(GameUpdater, makeGameUpdater)
