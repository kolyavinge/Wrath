from OpenGL.GL import GL_TEXTURE0

from game.calc.Vector3 import Vector3
from game.gl.BufferIndices import BufferIndices
from game.gl.ColorVector4 import ColorVector4
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory


class SpriteRenderer:

    def __init__(
        self,
        vboUpdaterFactory: VBOUpdaterFactory,
        vboRenderer: VBORenderer,
    ):
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.vboRenderer = vboRenderer
        maxLength = 500
        indices = [BufferIndices.vertices, BufferIndices.texCoords, BufferIndices.colors, BufferIndices.faces]
        self.vbo = self.vboUpdater.buildUnfilled(4 * maxLength, 2 * maxLength, indices)

    def init(self, rowSpritesCount, colSpritesCount, texture):
        self.texture = texture
        self.spriteWidth = texture.width / colSpritesCount
        self.spriteHeight = texture.height / rowSpritesCount
        self.textureXStep = 1.0 / (texture.width / self.spriteWidth)
        self.textureYStep = 1.0 / (texture.height / self.spriteHeight)

    def render(self, spriteItems):
        self.texture.bind(GL_TEXTURE0)
        self.vbo.reset()
        self.fillVBO(spriteItems)
        self.vboRenderer.render(self.vbo)

    def fillVBO(self, spriteItems):
        for row, col, x, y, alpha in spriteItems:
            xCoord = col * self.textureXStep
            yCoord = 1.0 - (row * self.textureYStep) - self.textureYStep
            self.vboUpdater.beginUpdate(self.vbo)
            self.vboUpdater.addVertex(Vector3(x, y, 0))
            self.vboUpdater.addVertex(Vector3(x + self.spriteWidth, y, 0))
            self.vboUpdater.addVertex(Vector3(x + self.spriteWidth, y + self.spriteHeight, 0))
            self.vboUpdater.addVertex(Vector3(x, y + self.spriteHeight, 0))
            self.vboUpdater.addTexCoord(xCoord, yCoord)
            self.vboUpdater.addTexCoord(xCoord + self.textureXStep, yCoord)
            self.vboUpdater.addTexCoord(xCoord + self.textureXStep, yCoord + self.textureYStep)
            self.vboUpdater.addTexCoord(xCoord, yCoord + self.textureYStep)
            self.vboUpdater.addColor(ColorVector4(1, 1, 1, alpha))
            self.vboUpdater.addColor(ColorVector4(1, 1, 1, alpha))
            self.vboUpdater.addColor(ColorVector4(1, 1, 1, alpha))
            self.vboUpdater.addColor(ColorVector4(1, 1, 1, alpha))
            self.vboUpdater.addFace(0, 1, 2)
            self.vboUpdater.addFace(0, 2, 3)
            self.vboUpdater.endUpdate()
