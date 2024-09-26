from game.calc.Vector3 import Vector3
from game.gl.VBOBuilderFactory import VBOBuilderFactory


class ScreenQuadVBO:

    def __init__(self, vboBuilderFactory):
        vboBulder = vboBuilderFactory.makeVBOBuilder()

        vboBulder.addVertex(Vector3(-1, -1, 0))
        vboBulder.addVertex(Vector3(1, -1, 0))
        vboBulder.addVertex(Vector3(1, 1, 0))
        vboBulder.addVertex(Vector3(-1, 1, 0))

        vboBulder.addNormal(Vector3(0, 0, 1))
        vboBulder.addNormal(Vector3(0, 0, 1))
        vboBulder.addNormal(Vector3(0, 0, 1))
        vboBulder.addNormal(Vector3(0, 0, 1))

        vboBulder.addFace(0, 1, 2)
        vboBulder.addFace(0, 2, 3)

        self.vbo = vboBulder.build()


def makeScreenQuadVBO(resolver):
    return ScreenQuadVBO(resolver.resolve(VBOBuilderFactory))
