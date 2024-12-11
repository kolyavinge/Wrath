from game.model.Material import Material


class BulletHoleInfo:

    def __init__(self, material, halfSize):
        self.material = material
        self.halfSize = halfSize


BulletHoleInfo.smallHole = BulletHoleInfo(Material.bulletHole, 0.02)
BulletHoleInfo.largeHole = BulletHoleInfo(Material.bulletHole, 0.05)
BulletHoleInfo.plasmaHole = BulletHoleInfo(Material.blackHole, 0.1)
BulletHoleInfo.explosionHole = BulletHoleInfo(Material.explosionHole, 1.0)
BulletHoleInfo.railgunHole = BulletHoleInfo(Material.blackHole, 0.05)

BulletHoleInfo.allItems = [
    BulletHoleInfo.smallHole,
    BulletHoleInfo.largeHole,
    BulletHoleInfo.plasmaHole,
    BulletHoleInfo.explosionHole,
    BulletHoleInfo.railgunHole,
]
