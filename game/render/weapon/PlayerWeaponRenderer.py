from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.weapon.WeaponRenderModel3dCollection import *


class PlayerWeaponRenderer:

    def __init__(self, gameData, weaponRenderModel3dCollection, vboRenderer):
        self.gameData = gameData
        self.weaponRenderModel3dCollection = weaponRenderModel3dCollection
        self.vboRenderer = vboRenderer

    def init(self):
        self.weaponRenderModel3dCollection.init()

    def render(self, shader):
        weaponType = type(self.gameData.playerItems.currentWeapon)
        model = self.weaponRenderModel3dCollection.getRenderModel3d(weaponType)
        for mesh in model.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)


def makePlayerWeaponRenderer(resolver):
    return PlayerWeaponRenderer(resolver.resolve(GameData), resolver.resolve(WeaponRenderModel3dCollection), resolver.resolve(VBORenderer))
