class RenderMesh:

    def __init__(self, vbo, texture, material):
        self.vbo = vbo
        self.texture = texture
        self.material = material

    def release(self):
        self.vbo.release()
        self.texture.release()


class RenderModel3d:

    def __init__(self, meshes, animations=None):
        self.meshes = meshes
        self.animations = animations

    def release(self):
        for m in self.meshes:
            m.release()
