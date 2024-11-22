from game.calc.Vector3 import Vector3
from game.gl.VBOBuilderFactory import VBOBuilderFactory


class ScreenQuadVBO:

    def __init__(self, vboBuilderFactory):
        vboBuilder = vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(-1, -1, 0))
        vboBuilder.addVertex(Vector3(1, -1, 0))
        vboBuilder.addVertex(Vector3(1, 1, 0))
        vboBuilder.addVertex(Vector3(-1, 1, 0))

        vboBuilder.addNormal(Vector3(0, 0, 1))
        vboBuilder.addNormal(Vector3(0, 0, 1))
        vboBuilder.addNormal(Vector3(0, 0, 1))
        vboBuilder.addNormal(Vector3(0, 0, 1))

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        self.vbo = vboBuilder.build()


def makeScreenQuadVBO(resolver):
    return ScreenQuadVBO(resolver.resolve(VBOBuilderFactory))
