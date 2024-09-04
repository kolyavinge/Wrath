from game.model.Material import Material


class LevelItemGroup:

    def __init__(self):
        self.material = Material.blank
        self.texture = None
        self.vbo = None

    def release(self):
        for vbo in self.vboList:
            vbo.release()
