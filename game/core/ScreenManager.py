from game.render.ui.GameScreenRenderer import GameScreenRenderer
from game.ui.GameScreen import GameScreen
from game.vox.ui.GameScreenVox import GameScreenVox


class ScreenManager:

    def __init__(
        self,
        gameScreen: GameScreen,
        gameScreenRenderer: GameScreenRenderer,
        gameScreenVox: GameScreenVox,
    ):
        self.screens = {}
        self.screens[GameScreen] = gameScreen
        for screen in self.screens.values():
            screen.screenManager = self

        self.screenRenderers = {}
        self.screenRenderers[GameScreen] = gameScreenRenderer

        self.screenVoxes = {}
        self.screenVoxes[GameScreen] = gameScreenVox

        self.changeScreen(GameScreen)

    def changeScreen(self, screenType):
        self.currentScreen = self.screens[screenType]
        self.currentScreen.activate()
        self.currentScreenRenderer = self.screenRenderers[screenType]
        self.currentScreenVox = self.screenVoxes[screenType]
