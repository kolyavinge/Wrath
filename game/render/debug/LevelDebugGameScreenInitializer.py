from game.engine.GameState import GameState
from game.render.debug.LevelDebugLevelSegmentRenderer import *
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class LevelDebugGameScreenInitializer:

    def __init__(
        self,
        gameState: GameState,
        levelDebugLevelSegmentRenderer: LevelDebugLevelSegmentRenderer,
        levelItemRenderCollection: LevelItemRenderCollection,
        shadowCasterRenderCollection: ShadowCasterRenderCollection,
        enemyRenderCollection: EnemyRenderCollection,
        enemyAnimationCollection: EnemyAnimationCollection,
    ):
        self.gameState = gameState
        self.levelDebugLevelSegmentRenderer = levelDebugLevelSegmentRenderer
        self.levelItemRenderCollection = levelItemRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.enemyRenderCollection = enemyRenderCollection
        self.enemyAnimationCollection = enemyAnimationCollection

    def init(self):
        allLevelSegments = self.gameState.visibilityTree.allLevelSegments
        self.levelDebugLevelSegmentRenderer.init(allLevelSegments)
        self.levelItemRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
        self.enemyRenderCollection.init()
        self.enemyAnimationCollection.init()
