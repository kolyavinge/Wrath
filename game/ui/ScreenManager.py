from game.ui.GameScreen import GameScreen


class ScreenManager:

    def __init__(self, gameScreen):
        self.screens = {}
        self.screens[GameScreen] = gameScreen
        for screen in self.screens.keys():
            screen.screenManager = self
        self.changeScreen(GameScreen)

    def changeScreen(self, screenType):
        self.currentScreen = self.screens[screenType]
        self.currentScreen.activate()


def makeScreenManager(resolver):
    return ScreenManager(resolver.resolve(GameScreen))
