from game.calc.Vector3 import Vector3
from game.lib.Random import Random


class WeaponFeedbackLogic:

    def __init__(self):
        self.rand = Random()

    def applyFeedback(self, weapon):
        newJitter = self.getNewJitter(weapon)
        newFeedback = self.getNewFeedback(newJitter, weapon)
        weapon.jitter.add(newJitter)
        weapon.feedback.add(newFeedback)

    def getNewJitter(self, weapon):
        x = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)
        y = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)
        z = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)

        return Vector3(x, y, z)

    def getNewFeedback(self, newJitter, weapon):
        newFeedback = weapon.direction.copy()
        newFeedback.add(newJitter)
        newFeedback.setLength(weapon.feedbackLength)
        newFeedback.mul(-1)

        return newFeedback


def makeWeaponFeedbackLogic(resolver):
    return WeaponFeedbackLogic()
