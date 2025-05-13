from OpenGL.GL import GL_TEXTURE0

from game.gl.vbo.VBORenderer import VBORenderer


class Model3dRenderer:

    def __init__(self, vboRenderer: VBORenderer):
        self.vboRenderer = vboRenderer

    def render(self, model, shader):
        for mesh in model.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)
