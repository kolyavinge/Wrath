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

    def init(self, gameState):
        self.gameState = gameState

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.gameState.camera, self.defaultAimStateFunc, self.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(self.gameState, shader)

    def renderShadowCasters(self, shader):
        self.levelSegmentRenderer.renderShadowCasters(self.gameState.playerItems, self.gameState.visibleLevelSegments, shader)
