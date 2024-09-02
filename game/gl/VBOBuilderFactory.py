from game.gl.VBOBuilder import VBOBuilder


class VBOBuilderFactory:

    def makeVBOBuilder(self):
        return VBOBuilder()


def makeVBOBuilderFactory(resolver):
    return VBOBuilderFactory()
