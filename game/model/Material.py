class Material:

    def __init__(self, ambient, diffuse, specular, shininess):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess


Material.blank = Material(1.0, 1.0, 1.0, 1.0)
Material.wallMetal1 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal2 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal3 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal4 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal5 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal6 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal7 = Material(0.2, 1.0, 0.5, 8.0)
Material.wallMetal8 = Material(0.2, 1.0, 0.5, 8.0)
Material.floorMetal1 = Material(0.2, 0.5, 0.5, 8.0)
Material.floorMetal2 = Material(0.2, 0.5, 0.5, 8.0)
Material.floorMetal3 = Material(0.2, 1.0, 0.5, 8.0)
Material.floorMetal4 = Material(0.2, 1.0, 0.5, 8.0)
Material.floorMetal5 = Material(0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal1 = Material(0.2, 1.0, 0.5, 8.0)
Material.ceilingMetal2 = Material(0.2, 1.0, 0.5, 8.0)
Material.edgeMetal1 = Material(0.2, 1.0, 0.5, 8.0)
Material.edgeMetal2 = Material(0.2, 1.0, 0.5, 8.0)
