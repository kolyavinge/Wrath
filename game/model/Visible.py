from game.model.Material import Material


# TODO унаследовать все видимые обьекты от этого класса
class Visible:

    def __init__(self):
        self.material = Material.blank
        self.canCastShadow = False
