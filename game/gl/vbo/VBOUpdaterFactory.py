from game.gl.vbo.VBOUpdater import VBOUpdater


class VBOUpdaterFactory:

    def makeVBOUpdater(self):
        return VBOUpdater()


def makeVBOUpdaterFactory(resolver):
    return VBOUpdaterFactory()
