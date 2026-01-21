from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.person.EnemyRenderer import EnemyRenderer


class LevelDebugLevelSegmentRenderer:

    def __init__(
        self,
        levelItemRenderer: LevelItemRenderer,
        enemyRenderer: EnemyRenderer,
        shadowCasterRenderer: ShadowCasterRenderer,
    ):
        self.levelItemRenderer = levelItemRenderer
        self.enemyRenderer = enemyRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def render(self, gameState, shader):
        for levelSegment in gameState.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, gameState.playerItems.torch)
            self.levelItemRenderer.render(shader, levelSegment)
            self.enemyRenderer.render(shader, levelSegment, gameState.player, gameState.camera, gameState.globalTimeMsec)

    def renderShadowCasters(self, playerItems, visibleLevelSegments, shader):
        for levelSegment in visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, playerItems.torch)
            self.shadowCasterRenderer.render(shader, levelSegment)
