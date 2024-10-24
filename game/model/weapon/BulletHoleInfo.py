from game.model.Material import Material


class BulletHoleInfo:

    def __init__(self, material, halfSize):
        self.material = material
        self.halfSize = halfSize


BulletHoleInfo.tinyHole = BulletHoleInfo(Material.tinyBulletHole, 0.05)

BulletHoleInfo.allItems = [BulletHoleInfo.tinyHole]
