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
Material.floorMetal1 = Material(0.2, 0.5, 0.5, 8.0)
Material.floorMetal2 = Material(0.2, 0.5, 0.5, 8.0)
Material.ceilingMetal1 = Material(0.2, 1.0, 0.5, 8.0)
Material.edgeMetal1 = Material(0.2, 1.0, 0.5, 8.0)
