from game.engine.GameData import GameData
from game.render.debug.LevelDebugLevelSegmentRenderer import *
from game.render.level.LevelItemRenderCollection import LevelItemRenderCollection
from game.render.level.ShadowCasterRenderCollection import ShadowCasterRenderCollection


class LevelDebugGameScreenInitializer:

    def __init__(
        self,
        gameData: GameData,
        levelDebugLevelSegmentRenderer: LevelDebugLevelSegmentRenderer,
        levelItemRenderCollection: LevelItemRenderCollection,
        shadowCasterRenderCollection: ShadowCasterRenderCollection,
    ):
        self.gameData = gameData
        self.levelDebugLevelSegmentRenderer = levelDebugLevelSegmentRenderer
        self.levelItemRenderCollection = levelItemRenderCollection
        self.shadowCasterRenderCollection = shadowCasterRenderCollection

    def init(self):
        allLevelSegments = self.gameData.visibilityTree.getAllLevelSegments()
        self.levelDebugLevelSegmentRenderer.init(allLevelSegments)
        self.levelItemRenderCollection.init(allLevelSegments)
        self.shadowCasterRenderCollection.init(allLevelSegments)
