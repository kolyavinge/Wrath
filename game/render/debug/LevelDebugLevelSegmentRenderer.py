from OpenGL.GL import *

from game.engine.GameData import GameData
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer


class LevelDebugLevelSegmentRenderer:

    def __init__(
        self,
        gameData: GameData,
        levelItemRenderer: LevelItemRenderer,
        shadowCasterRenderer: ShadowCasterRenderer,
    ):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def init(self, allLevelSegments):
        self.allLevelSegments = allLevelSegments

    def render(self, shader):
        for levelSegment in self.allLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.levelItemRenderer.render(shader, levelSegment)

    def renderShadowCasters(self, shader):
        for levelSegment in self.allLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.playerTorch)
            self.shadowCasterRenderer.render(levelSegment)
