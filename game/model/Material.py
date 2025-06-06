class MaterialKind:

    none = 0
    concrete = 1
    metal = 2


class Material:

    def __init__(self, kind, ambient=0.1, diffuse=0.8, specular=0.8, shininess=8.0):
        self.kind = kind
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess


Material.blank = Material(MaterialKind.metal, 1.0, 1.0, 1.0, 1.0)

Material.construction1 = Material(MaterialKind.metal)
Material.construction2 = Material(MaterialKind.metal)
Material.construction3 = Material(MaterialKind.metal)
Material.construction4 = Material(MaterialKind.metal)
Material.construction5 = Material(MaterialKind.metal)
Material.construction6 = Material(MaterialKind.metal)
Material.construction7 = Material(MaterialKind.metal)
Material.construction8 = Material(MaterialKind.metal)
Material.construction9 = Material(MaterialKind.metal)
Material.construction10 = Material(MaterialKind.metal, 0.2, 0.5, 0.5, 8.0)
Material.construction11 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.construction12 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.construction13 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.construction14 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.construction15 = Material(MaterialKind.metal)
Material.construction16 = Material(MaterialKind.metal)
Material.construction17 = Material(MaterialKind.metal)

Material.rock1 = Material(MaterialKind.concrete)

Material.edgeMetal1 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)

Material.weapon = Material(MaterialKind.metal, 0.2, 0.2, 0.2, 8.0)

Material.plasmaBullet = Material(MaterialKind.none, 1.0, 0.0, 0.0, 1.0)
Material.launcherBullet = Material(MaterialKind.none, 0.2, 0.5, 0.5, 8.0)

Material.commonBulletTrace = Material(MaterialKind.none, 0.2, 1.0, 0.5, 0.0)
Material.railgunBulletTrace = Material(MaterialKind.none, 1.0, 0.0, 0.0, 0.0)

Material.powerup = Material(MaterialKind.metal, 0.2, 0.1, 0.1, 8.0)

Material.bulletHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
Material.blackHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
Material.explosionHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)

Material.person = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
