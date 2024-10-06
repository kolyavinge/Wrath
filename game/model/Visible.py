from game.model.Material import Material


class Visible:

    def __init__(self):
        self.material = Material.blank
        self.defaultVisualSize = 10.0
        self.canCastShadow = False
