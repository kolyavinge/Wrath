class MaterialKind:

    concrete = 1
    metal = 2


class Material:

    def __init__(self, kind, ambient, diffuse, specular, shininess):
        self.kind = kind
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess


Material.blank = Material(MaterialKind.metal, 1.0, 1.0, 1.0, 1.0)
Material.wallMetal1 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal2 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal3 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal4 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal5 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal6 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal7 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal8 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.wallMetal9 = Material(MaterialKind.metal, 0.2, 0.8, 0.5, 8.0)
Material.floorConcrete1 = Material(MaterialKind.concrete, 0.2, 0.5, 0.5, 8.0)
Material.floorMetal2 = Material(MaterialKind.metal, 0.2, 0.5, 0.5, 8.0)
Material.floorMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.floorMetal4 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.floorMetal5 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal1 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal1 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal2 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
Material.edgeMetal3 = Material(MaterialKind.metal, 0.2, 1.0, 0.5, 8.0)
