from game.render.gl.vbo.VBOUpdater import VBOUpdater


class VBOUpdaterFactory:

    def makeVBOUpdater(self):
        return VBOUpdater()
