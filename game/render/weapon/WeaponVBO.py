class WeaponVBO:

    def __init__(self, texturedVBOs):
        self.texturedVBOs = texturedVBOs

    def release(self):
        for tv in self.texturedVBOs:
            tv.vbo.release()
            tv.texture.release()
