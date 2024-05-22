from game.core.GameFactory import GameFactory


class App:

    def run(self):
        gameFactory = GameFactory()
        self.game = gameFactory.makeGame()


app = App()
app.run()
