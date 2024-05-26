import os
from game.lib.Environment import Environment
from game.core.GameFactory import GameFactory


class App:

    def __init__(self):
        Environment.programRootPath = os.path.dirname(__file__)

    def run(self):
        gameFactory = GameFactory()
        self.game = gameFactory.makeGame()


app = App()
app.run()
