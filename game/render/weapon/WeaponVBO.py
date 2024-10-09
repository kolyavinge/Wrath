class WeaponVBO:

    def __init__(self, vbo, texture):
        self.vbo = vbo
        self.texture = texture

    def release(self):
        self.vbo.release()
