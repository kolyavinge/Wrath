from OpenGL.GL import *

from game.engine.GameData import GameData


class BulletTraceRenderer:

    def __init__(self, gameData):
        self.gameData = gameData

    def render(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)

        traces = self.getVisibleTraces()
        for trace in traces:
            self.renderTrace(trace)

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def renderTrace(self, trace):
        pass

    def getVisibleTraces(self):
        result = set()
        for levelSegment in self.gameData.visibleLevelSegments:
            for trace in levelSegment.bulletTraces:
                result.add(trace)

        return result


def makeBulletTraceRenderer(resolver):
    return BulletTraceRenderer(resolver.resolve(GameData))
