from game.model.Material import Material


class BulletHoleInfo:

    def __init__(self, material, halfSize):
        self.material = material
        self.halfSize = halfSize


BulletHoleInfo.smallHole = BulletHoleInfo(Material.bulletHole, 0.05)
BulletHoleInfo.largeHole = BulletHoleInfo(Material.bulletHole, 0.1)
BulletHoleInfo.plasmaHole = BulletHoleInfo(Material.plasmaHole, 0.1)
BulletHoleInfo.explosionHole = BulletHoleInfo(Material.explosionHole, 1.0)

BulletHoleInfo.allItems = [BulletHoleInfo.smallHole, BulletHoleInfo.largeHole, BulletHoleInfo.plasmaHole, BulletHoleInfo.explosionHole]
