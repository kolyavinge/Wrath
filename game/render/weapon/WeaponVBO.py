class WeaponVBO:

    def __init__(self, vbos, texture):
        self.vbos = vbos
        self.texture = texture

    def release(self):
        for vbo in self.vbos:
            vbo.release()
