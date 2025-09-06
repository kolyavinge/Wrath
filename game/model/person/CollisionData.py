class CollisionData:

    def __init__(self):
        self.personBullet = {}
        self.personPerson = {}
        self.personWalls = {}

    def clear(self):
        self.personBullet.clear()
        self.personPerson.clear()
        self.personWalls.clear()
