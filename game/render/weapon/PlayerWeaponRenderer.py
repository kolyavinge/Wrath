from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class PlayerWeaponRenderer:

    def __init__(self, gameData, renderCollection, vboRenderer):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def init(self):
        self.renderCollection.init()

    def render(self, shader):
        weapon = self.gameData.playerItems.currentWeapon
        shader.setModelMatrix(weapon.getModelMatrix())
        model = self.renderCollection.getRenderModel3d(type(weapon))
        for mesh in model.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)


def makePlayerWeaponRenderer(resolver):
    return PlayerWeaponRenderer(resolver.resolve(GameData), resolver.resolve(WeaponRenderCollection), resolver.resolve(VBORenderer))
