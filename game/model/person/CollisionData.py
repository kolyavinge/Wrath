class CollisionData:

    def __init__(self):
        self.personBullet = {}
        self.personRay = {}
        self.personExplosion = {}
        self.personPerson = {}
        self.personWalls = {}
        self.personFalling = set()

    def clear(self):
        self.personBullet.clear()
        self.personRay.clear()
        self.personExplosion.clear()
        self.personPerson.clear()
        self.personWalls.clear()
        self.personFalling.clear()
