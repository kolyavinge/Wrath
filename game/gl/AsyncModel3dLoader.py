from threading import Thread

from game.gl.Model3dLoader import Model3dLoader


class AsyncModel3dLoader:

    def __init__(self, model3dLoader):
        self.model3dLoader = model3dLoader

    def loadAsync(self, modelNames):
        self.result = {}

        def load(modelName):
            self.result[modelName] = self.model3dLoader.load(modelName)

        threads = []
        for modelName in modelNames:
            thread = Thread(target=lambda: load(modelName))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return self.result


def makeAsyncModel3dLoader(resolver):
    return AsyncModel3dLoader(resolver.resolve(Model3dLoader))
