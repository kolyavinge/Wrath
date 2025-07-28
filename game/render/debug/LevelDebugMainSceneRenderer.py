from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer


class LevelDebugMainSceneRenderer:

    def __init__(
        self,
        shadowedObjectRenderer: ShadowedObjectRenderer,
        levelSegmentRenderer: LevelSegmentRenderer,
    ):
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelSegmentRenderer = levelSegmentRenderer

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.defaultAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
