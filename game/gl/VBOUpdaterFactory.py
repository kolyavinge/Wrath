from game.gl.VBOUpdater import VBOUpdater


class VBOUpdaterFactory:

    def makeVBOUpdater(self):
        return VBOUpdater()


def makeVBOUpdaterFactory(resolver):
    return VBOUpdaterFactory()
