from game.engine.GameData import GameData
from game.lib.Query import Query
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.person.EnemyRenderer import EnemyRenderer
from game.render.powerup.PowerupRenderer import PowerupRenderer
from game.render.weapon.BulletRenderer import BulletRenderer


class LevelSegmentRenderer:

    def __init__(
        self,
        gameData: GameData,
        levelItemRenderer: LevelItemRenderer,
        bulletRenderer: BulletRenderer,
        powerupRenderer: PowerupRenderer,
        enemyRenderer: EnemyRenderer,
        shadowCasterRenderer: ShadowCasterRenderer,
    ):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.bulletRenderer = bulletRenderer
        self.powerupRenderer = powerupRenderer
        self.enemyRenderer = enemyRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def render(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.levelItemRenderer.render(shader, levelSegment)
            self.bulletRenderer.render(shader, levelSegment)
            self.powerupRenderer.render(shader, levelSegment)
            self.enemyRenderer.render(shader, levelSegment)

        # self.printDebugInfo()

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.shadowCasterRenderer.render(shader, levelSegment)
            self.powerupRenderer.renderForShadow(shader, levelSegment)
            self.enemyRenderer.renderForShadow(shader, levelSegment)

    def printDebugInfo(self):
        constructions = Query([segment.allConstructions for segment in self.gameData.visibleLevelSegments]).flatten().result
        print(f"all {len(constructions)}, unique {len(set(constructions))} {(len(set(constructions)) / len(constructions)):f}")
