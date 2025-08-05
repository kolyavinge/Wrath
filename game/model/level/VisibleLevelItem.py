from game.model.Material import Material


class VisibleLevelItem:

    def __init__(self):
        self.material = Material.blank
        self.canCastShadow = False
