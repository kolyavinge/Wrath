from game.vox.common.PersonVox import PersonVox
from game.vox.common.WeaponVox import WeaponVox


class VoxManager:

    def __init__(
        self,
        personVox: PersonVox,
        weaponVox: WeaponVox,
    ):
        self.personVox = personVox
        self.weaponVox = weaponVox

    def addPerson(self, person):
        self.personVox.addPerson(person)
        self.weaponVox.addPerson(person)

    def removePerson(self, person):
        self.personVox.removePerson(person)
        self.weaponVox.removePerson(person)
