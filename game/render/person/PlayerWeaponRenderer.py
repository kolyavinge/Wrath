from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.MeshLoader import MeshLoader
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.gl.VBORenderer import VBORenderer
from game.model.Material import Material


class PlayerWeaponRenderer:

    def __init__(self, gameData, meshLoader, vboBuilderFactory, vboRenderer):
        self.gameData = gameData
        self.meshLoader = meshLoader
        self.vboBuilderFactory = vboBuilderFactory
        self.vboRenderer = vboRenderer

    def init(self):
        mesh = self.meshLoader.load("")
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        self.vbo = vboBuilder.build()
        self.mainMaterial = Material.weapon
        self.mainTexture = mesh.mainTexture

    def render(self, shader):
        shader.setMaterial(self.mainMaterial)
        return
        self.mainTexture.bind(GL_TEXTURE0)
        self.vboRenderer.render(self.vbo)


def makePlayerWeaponRenderer(resolver):
    return PlayerWeaponRenderer(
        resolver.resolve(GameData), resolver.resolve(MeshLoader), resolver.resolve(VBOBuilderFactory), resolver.resolve(VBORenderer)
    )
