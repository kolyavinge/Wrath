from game.engine.GameData import GameData
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.person.EnemyRenderer import EnemyRenderer


class LevelDebugLevelSegmentRenderer:

    def __init__(
        self,
        gameData: GameData,
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
            shader.setLight(levelSegment.lights, self.gameData.playerTorch)
            self.shadowCasterRenderer.render(levelSegment)
