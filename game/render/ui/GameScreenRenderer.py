from game.render.debug.DebugRenderer import DebugRenderer
from game.render.level.LevelRenderer import LevelRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer


class GameScreenRenderer:

    def __init__(self, debugRenderer, levelRenderer, mainSceneRenderer):
        self.debugRenderer = debugRenderer
        self.levelRenderer = levelRenderer
        self.mainSceneRenderer = mainSceneRenderer

    def init(self):
        self.levelRenderer.init()
        self.mainSceneRenderer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(resolver.resolve(DebugRenderer), resolver.resolve(LevelRenderer), resolver.resolve(MainSceneRenderer))
