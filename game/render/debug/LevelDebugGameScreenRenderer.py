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

    def init(self):
        self.gameScreenInitializer.init()

    def render(self):
        self.mainSceneRenderer.renderDefaultAimState()
        self.backgroundRenderer.render()
