from game.model.weapon.Weapon import FireState


class WeaponAltFireStateSwitcher:

    def switch(self, weapon, isAltFireOn):
        state = weapon.altFireState

        if isAltFireOn:
            if state == FireState.deactive:
                state = FireState.activated
            elif state == FireState.activated:
                state = FireState.active
            elif state == FireState.active:
                state = FireState.active
            elif state == FireState.deactivated:
                state = FireState.activated
            else:
                assert False
        else:
            if state == FireState.deactive:
                state = FireState.deactive
            elif state == FireState.activated:
                state = FireState.deactivated
            elif state == FireState.active:
                state = FireState.deactivated
            elif state == FireState.deactivated:
                state = FireState.deactive
            else:
                assert False

        weapon.altFireState = state
