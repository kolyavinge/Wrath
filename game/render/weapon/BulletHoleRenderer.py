from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.vbo.VBORenderer import VBORenderer
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection


class BulletHoleRenderer:

    def __init__(
        self,
        bulletHoleRenderCollection: BulletHoleRenderCollection,
        vboRenderer: VBORenderer,
    ):
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        shader.setModelMatrix(TransformMatrix4.identity)
        meshes = self.bulletHoleRenderCollection.getRenderMeshes(levelSegment)
        for mesh in meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
