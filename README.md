# BadUsbDemo

## Prepare
1. RP2040
2. https://circuitpython.org/board/raspberry_pi_pico/
3. https://github.com/adafruit/Adafruit_CircuitPython_HID

## Step-by-step guide
1. Get uf2 file from https://circuitpython.org/board/raspberry_pi_pico/
2. Press BOOT button on the board and connect it to the host
3. Copy uf2 file to the root of the device
4. Plug-out and plug-in RP2040
5. Copy https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid folder to the /lib folder
6. Copy code from the repo to the code.py on the RP2040
