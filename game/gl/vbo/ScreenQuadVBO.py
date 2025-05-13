from game.calc.Vector3 import Vector3
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory


class ScreenQuadVBO:

    def __init__(self, vboBuilderFactory: VBOBuilderFactory):
        vboBuilder = vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(-1, -1, 0))
        vboBuilder.addVertex(Vector3(1, -1, 0))
        vboBuilder.addVertex(Vector3(1, 1, 0))
        vboBuilder.addVertex(Vector3(-1, 1, 0))

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        self.vbo = vboBuilder.build()
