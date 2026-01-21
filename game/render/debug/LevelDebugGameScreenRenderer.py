from game.render.level.BackgroundRenderer import BackgroundRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer


class LevelDebugGameScreenRenderer:

    def __init__(
        self,
        gameScreenInitializer: GameScreenInitializer,
        backgroundRenderer: BackgroundRenderer,
        mainSceneRenderer: MainSceneRenderer,
    ):
        self.gameScreenInitializer = gameScreenInitializer
        self.backgroundRenderer = backgroundRenderer
        self.mainSceneRenderer = mainSceneRenderer

    def init(self, gameState):
        self.gameScreenInitializer.init(gameState)

    def render(self, gameState):
        self.mainSceneRenderer.renderDefaultAimState()
        self.backgroundRenderer.render(gameState.backgroundVisibility, gameState.camera)
