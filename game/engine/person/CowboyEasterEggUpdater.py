from game.lib.Math import Math
from game.model.weapon.Pistol import Pistol


class CowboyEasterEggUpdater:

    # небольшая пасхалочка
    # если игрок стоит неподвижно с пистолетами 20 секунд, то он их начинает крутить

    def __init__(self):
        self.remainInit = 50
        self.radianStep = 5 * Math.piDouble / self.remainInit

    def update(self, gameState):
        playerItems = gameState.playerItems
        if type(playerItems.currentWeapon) != Pistol:
            return

        player = gameState.player
        anyActions = gameState.playerInputData.anyActions() or player.weaponSelectState is not None
        cowboyRemain = player.cowboyRemain

        if not anyActions and cowboyRemain.isExpired():
            if gameState.globalTimeMsec - player.noActionTime >= 20 * 1000:
                cowboyRemain.set(self.remainInit)
                player.noActionTime = gameState.globalTimeMsec
        elif not anyActions and not cowboyRemain.isExpired():
            radians = (self.remainInit - cowboyRemain.value) * self.radianStep
            playerItems.rightHandWeapon.pitchRadians += radians
            playerItems.leftHandWeapon.pitchRadians += radians
            cowboyRemain.decrease()
        elif anyActions and cowboyRemain.isExpired():
            player.noActionTime = gameState.globalTimeMsec
        elif anyActions and not cowboyRemain.isExpired():
            player.noActionTime = gameState.globalTimeMsec
            cowboyRemain.set(0)
