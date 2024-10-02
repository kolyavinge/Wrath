from game.render.debug.DebugRenderer import DebugRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer


class GameScreenRenderer:

    def __init__(self, debugRenderer, mainSceneRenderer):
        self.debugRenderer = debugRenderer
        self.mainSceneRenderer = mainSceneRenderer

    def init(self):
        self.mainSceneRenderer.init()

    def render(self):
        # self.debugRenderer.render()
        self.mainSceneRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(resolver.resolve(DebugRenderer), resolver.resolve(MainSceneRenderer))
