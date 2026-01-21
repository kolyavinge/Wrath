from game.render.debug.LevelDebugLevelSegmentRenderer import *
from game.render.level.BackgroundRenderer import BackgroundRenderer
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class LevelDebugGameScreenInitializer:

    def __init__(
        self,
        levelDebugLevelSegmentRenderer: LevelDebugLevelSegmentRenderer,
        levelItemRenderCollection: LevelItemRenderCollection,
        shadowCasterRenderCollection: ShadowCasterRenderCollection,
        backgroundRenderer: BackgroundRenderer,
        enemyRenderCollection: EnemyRenderCollection,
        enemyAnimationCollection: EnemyAnimationCollection,
        mainSceneRenderer: MainSceneRenderer,
    ):
        self.levelDebugLevelSegmentRenderer = levelDebugLevelSegmentRenderer
        self.levelItemRenderCollection = levelItemRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection
        self.backgroundRenderer = backgroundRenderer
        self.enemyRenderCollection = enemyRenderCollection
        self.enemyAnimationCollection = enemyAnimationCollection
        self.mainSceneRenderer = mainSceneRenderer

    def init(self, gameState):
        allLevelSegments = gameState.visibilityTree.allLevelSegments
        # self.levelDebugLevelSegmentRenderer.init(gameState.playerItems.torch, allLevelSegments)
        self.levelItemRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
        self.backgroundRenderer.init(gameState.backgroundVisibility)
        self.enemyRenderCollection.init()
        self.enemyAnimationCollection.init(gameState.enemies)
        self.mainSceneRenderer.init(gameState)
