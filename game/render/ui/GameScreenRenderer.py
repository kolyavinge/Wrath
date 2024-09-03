from game.render.debug.DebugRenderer import DebugRenderer
from game.render.level.LevelRenderer import LevelRenderer


class GameScreenRenderer:

    def __init__(self, debugRenderer, levelRenderer):
        self.debugRenderer = debugRenderer
        self.levelRenderer = levelRenderer

    def init(self):
        self.levelRenderer.init()

    def render(self):
        # self.debugRenderer.render()
        self.levelRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(resolver.resolve(DebugRenderer), resolver.resolve(LevelRenderer))
