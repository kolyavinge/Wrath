from game.calc.Vector3 import Vector3


class SnapshotBullet:

    def __init__(self, id=0, personId=0, weaponNumber=0, position=Vector3(), direction=Vector3()):
        self.id = id
        self.personId = personId
        self.weaponNumber = weaponNumber
        self.position = position
        self.direction = direction

    def __eq__(self, value):
        return (
            self.id == value.id
            and self.personId == value.personId
            and self.weaponNumber == value.weaponNumber
            and self.position == value.position
            and self.direction == value.direction
        )

    def __hash__(self):
        return hash(
            (
                self.id.__hash__(),
                self.personId.__hash__(),
                self.weaponNumber.__hash__(),
                self.position.__hash__(),
                self.direction.__hash__(),
            )
        )

