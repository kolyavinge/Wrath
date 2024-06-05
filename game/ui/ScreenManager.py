from game.ui.GameScreen import GameScreen


class ScreenManager:

    def __init__(self, gameScreen):
        self.screens = {}
        self.screens[GameScreen] = gameScreen
        for screen in self.screens.keys():
            screen.screenManager = self
        self.currentScreen = gameScreen

    def changeScreen(self, screenType):
        self.currentScreen = self.screens[screenType]


def makeScreenManager(resolver):
    return ScreenManager(resolver.resolve(GameScreen))
