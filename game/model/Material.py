class MaterialKind:

    none = 0
    concrete = 1
    metal = 2


class Material:

    def __init__(self, kind, ambient=0.2, diffuse=0.8, specular=0.1, shininess=2.0):
        self.kind = kind
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess


Material.blank = Material(MaterialKind.metal, 1.0, 1.0, 1.0, 1.0)

Material.wallMetal1 = Material(MaterialKind.metal)
Material.wallMetal2 = Material(MaterialKind.metal)
Material.wallMetal3 = Material(MaterialKind.metal)
Material.wallMetal4 = Material(MaterialKind.metal)
Material.wallMetal5 = Material(MaterialKind.metal)
Material.wallMetal6 = Material(MaterialKind.metal)
Material.wallMetal7 = Material(MaterialKind.metal)
Material.wallMetal8 = Material(MaterialKind.metal)
Material.wallMetal9 = Material(MaterialKind.metal)

Material.floorConcrete1 = Material(MaterialKind.concrete, 0.2, 0.5, 0.5, 8.0)
Material.floorMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.floorMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.floorMetal4 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.floorMetal5 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)

Material.ceilingMetal1 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)

Material.edgeMetal1 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)

Material.weapon = Material(MaterialKind.metal, 0.2, 0.2, 0.2, 8.0)

Material.plasmaBullet = Material(MaterialKind.none, 1.0, 0.0, 0.0, 1.0)
Material.launcherBullet = Material(MaterialKind.none, 0.2, 0.5, 0.5, 8.0)

Material.railgunBulletTrace = Material(MaterialKind.none, 1.0, 0.0, 0.0, 0.0)

Material.powerup = Material(MaterialKind.metal, 0.2, 0.1, 0.1, 8.0)

Material.bulletHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
Material.blackHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
Material.explosionHole = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)

Material.person = Material(MaterialKind.none, 0.2, 0.1, 0.1, 1.0)
