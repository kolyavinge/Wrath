from game.render.ui.GameScreenRenderer import GameScreenRenderer
from game.ui.GameScreen import GameScreen


class ScreenManager:

    def __init__(self, gameScreen, gameScreenRenderer):
        self.screens = {}
        self.screens[GameScreen] = gameScreen
        for screen in self.screens.values():
            screen.screenManager = self

        self.screenRenderers = {}
        self.screenRenderers[GameScreen] = gameScreenRenderer

        self.changeScreen(GameScreen)

    def changeScreen(self, screenType):
        self.currentScreen = self.screens[screenType]
        self.currentScreen.activate()
        self.currentScreenRenderer = self.screenRenderers[screenType]


def makeScreenManager(resolver):
    return ScreenManager(resolver.resolve(GameScreen), resolver.resolve(GameScreenRenderer))
