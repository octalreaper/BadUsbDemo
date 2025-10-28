import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
time.sleep(2)

NUMPAD = {
    '0': Keycode.KEYPAD_ZERO,
    '1': Keycode.KEYPAD_ONE,
    '2': Keycode.KEYPAD_TWO,
    '3': Keycode.KEYPAD_THREE,
    '4': Keycode.KEYPAD_FOUR,
    '5': Keycode.KEYPAD_FIVE,
    '6': Keycode.KEYPAD_SIX,
    '7': Keycode.KEYPAD_SEVEN,
    '8': Keycode.KEYPAD_EIGHT,
    '9': Keycode.KEYPAD_NINE
}

def send_alt_code(code_str):
    kbd.press(Keycode.ALT)
    time.sleep(0.005)
    for ch in code_str:
        kbd.press(NUMPAD[ch])
        kbd.release(NUMPAD[ch])
        time.sleep(0.005)

    kbd.release(Keycode.ALT)
    time.sleep(0.005)

def send_letter_via_alt(letter):
    ascii_code = ord(letter)
    code_str = f"{ascii_code:03d}"
    send_alt_code(code_str)
    time.sleep(0.005)

kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()

for ch in "powershell":
    send_letter_via_alt(ch)

kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
kbd.release_all()

time.sleep(0.5)
kbd.press(Keycode.LEFT_ARROW)
time.sleep(0.5)
kbd.release_all()

kbd.press(Keycode.ENTER)
time.sleep(0.1)
kbd.release_all()
