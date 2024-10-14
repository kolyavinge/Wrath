from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.model.Material import Material
from game.render.weapon.WeaponVBOCollection import WeaponVBOCollection


class PlayerWeaponRenderer:

    def __init__(self, gameData, weaponVBOCollection, vboRenderer):
        self.gameData = gameData
        self.weaponVBOCollection = weaponVBOCollection
        self.vboRenderer = vboRenderer

    def init(self):
        self.weaponVBOCollection.init()

    def render(self, shader):
        shader.setMaterial(Material.weapon)
        weaponType = type(self.gameData.playerItems.currentWeapon)
        weaponVBO = self.weaponVBOCollection.getWeaponVBO(weaponType)
        for tv in weaponVBO.texturedVBOs:
            tv.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(tv.vbo)


def makePlayerWeaponRenderer(resolver):
    return PlayerWeaponRenderer(resolver.resolve(GameData), resolver.resolve(WeaponVBOCollection), resolver.resolve(VBORenderer))
