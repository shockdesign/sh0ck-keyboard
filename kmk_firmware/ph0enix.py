# ph0enix designed by shockdesign & pelrun
# https://github.com/shockdesign/sh0ck-keyboard
# Requires CircuitPython 7.0.0 to support the RP2040 MCU

import board

import kb from KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP15,
    board.GP14, board.GP13, board.GP12, board.GP11
)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5)

FN = KC.MO(1)

keyboard.keymap = [
    # Qwerty
    # ,----------------------------------------------------------------------------.
    # | ESC  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------+------+------+------+------+------+------|
    # | Tab  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  | Enter|
    # |------+------+------+------+------+-------------+------+------+------+------|
    # | Shift|   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   Up |   .  |
    # |------+------+------+------+------+------+------+------+------+------+------|
    # | Ctrl |  Alt |  GUI | Space|   FN | Space|   /  | Left | Down | Right| Bksp |
    # `----------------------------------------------------------------------------'
    [
        KC.GESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.TAB,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    KC.ENT,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    KC.COMM, KC.UP,   KC.DOT,
        KC.LCTRL, KC.LALT, KC.LGUI, KC.SPC,  FN,      KC.SPC, KC.SLSH, KC.LEFT, KC.DOWN, KC.RGHT, KC.BSPC,
    ],
    # Alt
    # ,----------------------------------------------------------------------------.
    # | Grave|   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |
    # |------+------+------+------+------+------+------+------+------+------+------|
    # | Trans|   F1 |   F3 |   F5 |   F7 |   F9 |  F11 | Trans| Trans| Trans| Trans|
    # |------+------+------+------+------+-------------+------+------+------+------|
    # | Trans|   F2 |   F4 |   F6 |   F8 |  F10 |  F12 | Trans|   (  | Trans|   )  |
    # |------+------+------+------+------+------+------+------+------+------+------|
    # | Trans| Trans| Trans| Trans| Trans| Trans|   \  | Trans| Trans| Trans| Trans|
    # `----------------------------------------------------------------------------'
    [
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,    KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.TRNS, KC.F1,   KC.F3,   KC.F5,    KC.F7,   KC.F9,   KC.F11,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.F2,   KC.F4,   KC.F6,    KC.F8,   KC.F10,  KC.F12,  KC.TRNS, KC.LBRC, KC.TRNS, KC.RBRC,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.BSLS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
