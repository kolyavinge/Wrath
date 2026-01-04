from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.GameState import GameState
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.person.BloodStain import BloodStain


class PlayerBloodStainUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        self.updateBloodStains()
        if self.canAddNewBloodStain():
            self.addNewBloodStain()

    def updateBloodStains(self):
        for bloodStain in self.gameState.bloodStains:
            bloodStain.brightness *= bloodStain.fade
            if bloodStain.brightness < 0.1:
                self.gameState.bloodStains.remove(bloodStain)

    def addNewBloodStain(self):
        bloodStain = BloodStain()
        bloodStain.number = Random.getInt(0, BloodStain.numbersCount - 1)
        bloodStain.position = Vector3(0.5 + Random.getFloat(-0.4, 0.4), 0.5 + Random.getFloat(-0.4, 0.4), 0.0)
        bloodStain.brightness = 1.0
        bloodStain.fade = Random.getFloat(0.95, 0.99)
        bloodStain.radians = Random.getFloat(-Math.piDouble, Math.piDouble)
        bloodStain.scaleVector = Vector3(Random.getFloat(0.5, 2.0), Random.getFloat(0.5, 2.0), 1.0)
        self.gameState.bloodStains.append(bloodStain)

    def canAddNewBloodStain(self):
        if len(self.gameState.bloodStains) >= CommonConstants.maxBloodStains:
            return False

        player = self.gameState.player
        collisionData = self.gameState.collisionData

        return (
            player in collisionData.personBullet
            or player in collisionData.personRay
            or player in collisionData.personExplosion
            or player in collisionData.personFalling
        )
