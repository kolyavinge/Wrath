import keyboard

from game.input.InputDevice import InputDevice


class KeyboardButtons:

    esc = b"\x1b"
    backspace = b"\x08"
    space = "space"

    d1 = "1"
    d2 = "2"
    d3 = "3"
    d4 = "4"
    d5 = "5"
    d6 = "6"

    w = "w"
    a = "a"
    s = "s"
    d = "d"
    f = "f"

    allButtons = [d1, d2, d3, d4, d5, d6, w, a, s, d, f, space]


class Keyboard(InputDevice):

    def __init__(self):
        super().__init__(KeyboardButtons.allButtons)

    def checkInnerPressed(self, button):
        return keyboard.is_pressed(button)
