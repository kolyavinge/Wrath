class WallInfo:

    def __init__(self, position, frontNormal, height, material, bottomBorder=None, topBorder=None, doorway=None, visualSize=2.0):
        self.position = position
        self.frontNormal = frontNormal
        self.height = height
        self.material = material
        self.bottomBorder = bottomBorder
        self.topBorder = topBorder
        self.doorway = doorway
        self.visualSize = visualSize
