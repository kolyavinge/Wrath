from game.engine.GameState import GameState
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.person.EnemyRenderer import EnemyRenderer


class LevelDebugLevelSegmentRenderer:

    def __init__(
        self,
        gameData: GameState,
        levelItemRenderer: LevelItemRenderer,
        enemyRenderer: EnemyRenderer,
        shadowCasterRenderer: ShadowCasterRenderer,
    ):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.enemyRenderer = enemyRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def init(self, allLevelSegments):
        self.allLevelSegments = allLevelSegments

    def render(self, shader):
        for levelSegment in self.allLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.levelItemRenderer.render(shader, levelSegment)
            self.enemyRenderer.render(shader, levelSegment)

    def renderShadowCasters(self, shader):
        for levelSegment in self.allLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.shadowCasterRenderer.render(levelSegment)
