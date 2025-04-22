from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData


class PersonWeaponPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        self.updateForPlayer()
        self.updateForEnemies()

    def updateForPlayer(self):
        self.updateForPerson(self.gameData.player)

    def updateForEnemies(self):
        for enemy in self.gameData.enemies:
            self.updateForPerson(enemy)

    def updateForPerson(self, person):
        personItems = self.gameData.allPersonItems[person]
        self.updateWeapon(person, personItems.rightHandWeapon, rightHand=True)
        if personItems.leftHandWeapon is not None:
            self.updateWeapon(person, personItems.leftHandWeapon, rightHand=False)

    def updateWeapon(self, person, weapon, rightHand):
        weaponPosition = self.getWeaponPosition(person, weapon, rightHand)
        barrelPosition = self.getBarrelPosition(person, weapon, weaponPosition, rightHand)
        aimPoint = self.getAimPoint(person, barrelPosition)

        weapon.position = weaponPosition
        weapon.barrelPosition = barrelPosition
        weapon.direction = weapon.position.getDirectionTo(aimPoint)
        weapon.direction.normalize()
        weapon.direction.add(weapon.jitter)
        weapon.direction.normalize()
        weapon.yawRadians = person.yawRadians
        weapon.pitchRadians = person.pitchRadians

        if not weapon.jitter.isZero():
            weapon.jitter.mul(weapon.jitterFade)

        if not weapon.feedback.isZero():
            weapon.feedback.mul(weapon.feedbackFade)

    def getWeaponPosition(self, person, weapon, rightHand):
        rightShift = person.rightNormal.copy()
        rightShift.mul(weapon.playerShift.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = person.lookDirection.copy()
        frontShift.mul(weapon.playerShift.y)
        topShift = person.lookDirectionNormal.copy()
        topShift.mul(weapon.playerShift.z)
        weaponPosition = person.eyePosition.copy()
        weaponPosition.add(rightShift)
        weaponPosition.add(frontShift)
        weaponPosition.add(topShift)
        weaponPosition.add(weapon.feedback)

        return weaponPosition

    def getBarrelPosition(self, person, weapon, weaponPosition, rightHand):
        rightShift = person.rightNormal.copy()
        rightShift.mul(weapon.barrelPoint.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = person.lookDirection.copy()
        frontShift.mul(weapon.barrelPoint.y)
        topShift = person.lookDirectionNormal.copy()
        topShift.mul(weapon.barrelPoint.z)
        barrelPosition = weaponPosition.copy()
        barrelPosition.add(rightShift)
        barrelPosition.add(frontShift)
        barrelPosition.add(topShift)

        return barrelPosition

    def getAimPoint(self, player, barrelPosition):
        aimPoint = player.lookDirection.copy()
        aimPoint.setLength(PersonConstants.aimLength)
        aimPoint.add(barrelPosition)

        return aimPoint


def makePersonWeaponPositionUpdater(resolver):
    return PersonWeaponPositionUpdater(resolver.resolve(GameData))
