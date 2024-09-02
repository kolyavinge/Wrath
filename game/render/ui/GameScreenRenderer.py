from game.render.level.LevelRenderer import LevelRenderer


class GameScreenRenderer:

    def __init__(self, levelRenderer):
        self.levelRenderer = levelRenderer

    def init(self):
        self.levelRenderer.init()

    def render(self):
        self.levelRenderer.render()


def makeGameScreenRenderer(resolver):
    return GameScreenRenderer(resolver.resolve(LevelRenderer))
