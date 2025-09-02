from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.model.person.Player import Player


class PersonWeaponPositionUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        self.updateForPlayer()
        self.updateForEnemies()

    def updateForPlayer(self):
        self.updateForPerson(self.gameData.player)

    def updateForEnemies(self):
        for enemy in self.gameData.enemies:
            if enemy.isVisibleForPlayer:
                self.updateForPerson(enemy)

    def updateForPerson(self, person):
        personItems = self.gameData.allPersonItems[person]
        self.updateWeapon(person, personItems.rightHandWeapon, rightHand=True)
        if personItems.leftHandWeapon is not None:
            self.updateWeapon(person, personItems.leftHandWeapon, rightHand=False)

    def updateWeapon(self, person, weapon, rightHand):
        personShift = weapon.playerShift if type(person) == Player else weapon.enemyShift
        weaponPosition = self.getWeaponPosition(person, personShift, weapon.feedback, rightHand)
        barrelPosition = self.getBarrelPosition(person, weapon.barrelPoint, weaponPosition, rightHand)
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

    def getWeaponPosition(self, person, personShift, feedback, rightHand):
        rightShift = person.rightNormal.copy()
        rightShift.mul(personShift.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = person.lookDirection.copy()
        frontShift.mul(personShift.y)
        topShift = person.lookDirectionNormal.copy()
        topShift.mul(personShift.z)
        breathShift = person.lookDirectionNormal.copy()
        breathShift.mul(person.breathFunc.getValue(person.breathTime))

        weaponPosition = person.eyePosition.copy()
        weaponPosition.add(rightShift)
        weaponPosition.add(frontShift)
        weaponPosition.add(topShift)
        weaponPosition.add(feedback)
        weaponPosition.add(breathShift)

        return weaponPosition

    def getBarrelPosition(self, person, barrelPoint, weaponPosition, rightHand):
        rightShift = person.rightNormal.copy()
        rightShift.mul(barrelPoint.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = person.lookDirection.copy()
        frontShift.mul(barrelPoint.y)
        topShift = person.lookDirectionNormal.copy()
        topShift.mul(barrelPoint.z)
        barrelPosition = weaponPosition.copy()
        barrelPosition.add(rightShift)
        barrelPosition.add(frontShift)
        barrelPosition.add(topShift)

        return barrelPosition

    def getAimPoint(self, person, barrelPosition):
        aimPoint = person.lookDirection.copy()
        aimPoint.setLength(PersonConstants.aimLength)
        aimPoint.add(barrelPosition)

        return aimPoint
