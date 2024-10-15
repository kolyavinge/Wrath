class RenderMesh:

    def __init__(self, vbo, texture, material):
        self.vbo = vbo
        self.texture = texture
        self.material = material

    def release(self):
        self.vbo.release()
        self.texture.release()


class RenderModel3d:

    def __init__(self, meshes):
        self.meshes = meshes

    def release(self):
        for m in self.meshes:
            m.release()
