from game.model.Material import Material


class Visible:

    def __init__(self):
        self.material = Material.blank
        self.canCastShadow = False
