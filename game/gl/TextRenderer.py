from OpenGL.GL import *

from game.calc.Vector3 import Vector3
from game.gl.BufferIndices import BufferIndices
from game.gl.TextureLoader import TextureLoader
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.Environment import Environment


class TextRenderer:

    def __init__(
        self,
        textureLoader: TextureLoader,
        vboUpdaterFactory: VBOUpdaterFactory,
        vboRenderer: VBORenderer,
    ):
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.vboRenderer = vboRenderer
        self.symbolCoordinates = self.getSymbolCoordinates()
        self.alphabetTexture = textureLoader.load(Environment.programRootPath + "\\res\\menu\\alphabet.png")
        self.symbolWidth = 64.0
        self.symbolHeight = 64.0
        self.spaceWidth = 38.0
        self.textureXStep = 1.0 / (self.alphabetTexture.width / self.symbolWidth)
        self.textureYStep = 1.0 / (self.alphabetTexture.height / self.symbolHeight)
        maxLength = 500
        self.vbo = self.vboUpdater.buildUnfilled(4 * maxLength, 2 * maxLength, [BufferIndices.vertices, BufferIndices.texCoords, BufferIndices.faces])

    def render(self, textItems):
        self.alphabetTexture.bind(GL_TEXTURE0)
        self.vbo.reset()
        self.fillVBO(textItems)
        self.vboRenderer.render(self.vbo)

    def fillVBO(self, textItems):
        for text, positionX, positionY in textItems:
            for symbIndex, symb in enumerate(text):
                if symb == " ":
                    continue
                alphSymbRow, alphSymbCol = self.symbolCoordinates[symb]
                x = positionX + symbIndex * self.spaceWidth
                xCoord = alphSymbCol * self.textureXStep
                yCoord = 1.0 - (alphSymbRow * self.textureYStep) - self.textureYStep
                self.vboUpdater.beginUpdate(self.vbo)
                self.vboUpdater.addVertex(Vector3(x, positionY, 0))
                self.vboUpdater.addVertex(Vector3(x + self.symbolWidth, positionY, 0))
                self.vboUpdater.addVertex(Vector3(x + self.symbolWidth, positionY + self.symbolHeight, 0))
                self.vboUpdater.addVertex(Vector3(x, positionY + self.symbolHeight, 0))
                self.vboUpdater.addTexCoord(xCoord, yCoord)
                self.vboUpdater.addTexCoord(xCoord + self.textureXStep, yCoord)
                self.vboUpdater.addTexCoord(xCoord + self.textureXStep, yCoord + self.textureYStep)
                self.vboUpdater.addTexCoord(xCoord, yCoord + self.textureYStep)
                self.vboUpdater.addFace(0, 1, 2)
                self.vboUpdater.addFace(0, 2, 3)
                self.vboUpdater.endUpdate()

    def getSymbolCoordinates(self):
        result = {}
        allSymbols = ["01234567", "89abcdef", "ghijklmn", "opqrstuv", "wxyz+-*/", "=()[]{}<", ">!?@#$%^", "&|\\:'"]
        for row, symbols in enumerate(allSymbols):
            for col, symb in enumerate(symbols):
                assert symb not in result
                result[symb] = (row, col)

        return result


def makeTextRenderer(resolver):
    return TextRenderer(
        resolver.resolve(TextureLoader),
        resolver.resolve(VBOUpdaterFactory),
        resolver.resolve(VBORenderer),
    )
