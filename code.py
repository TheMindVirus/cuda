# Adafruit Macropad RP2040
# CircuitPython7.0.0-rc1
# MicroPython v1.12-v1.18 (mpy=517)

import os, sys

__print__ = print
__log__ = ""
def print(*args):
    global __log__
    __print__(*args)
    __log__ += str(args)

print("[INFO]: __log__");
print(__log__)
__log__ = ""

__sys__ = sys
__syslog__ = ""
class sys:
    class stdout:
        def write(x):
            global __syslog__
            __sys__.stdout.write(x)
            __syslog__ += x

sys.stdout.write("[INFO]: __syslog__\n")
sys.stdout.write(__syslog__)
__syslog__ = ""

help()
help("modules")

print("[INFO]: len(__log__) = " + str(len(__log__)))
sys.stdout.write("[INFO]: len(__syslog__) = " + str(len(__syslog__)) + "\n")

"""
[INFO]: len(__log__) = 0
[INFO]: len(__syslog__) = 0
"""

# https://github.com/micropython/micropython/blob/b41aaaa8a918a6645ebc6bfa4483bd17286f9263/py/builtinhelp.c#L165
# "STATIC mp_obj_t mp_builtin_help(size_t n_args, const mp_obj_t *args) {"
# "mp_print_str(MP_PYTHON_PRINTER, MICROPY_PY_BUILTINS_HELP_TEXT);"

sys = __sys__
print = __print__

builtin_module_names = \
[
    "__main__", "bitops", "math", "sdcardio", "_bleio", "board",
    "microcontroller", "sharpdisplay",
    "adafruit_bus_device", "builtins", "micropython", "storage",
    "adafruit_pixelbuf", "busio", "msgpack", "struct",
    "aesio", "collections", "neopixel_write", "supervisor",
    "alarm", "countio", "onewireio", "synthio", "analogio", "digitalio",
    "os", "sys", "array", "displayio", "pulseio", "terminalio",
    "atexit", "errno", "pwmio", "time",
    "audiobusio", "fontio", "qrio", "touchio",
    "audiocore", "framebufferio", "rainbowio", "traceback",
    "audiomixer", "gc", "random", "ulab",
    "audiomp3", "getpass", "re", "usb_cdc",
    "audiopwmio", "imagecapture", "rgbmatrix", "usb_hid",
    "binascii", "io", "rotaryio", "usb_midi",
    "bitbangio", "json", "rp2pio", "vectorio",
    "bitmaptools", "keypad", "rtc", "watchdog"
]

for i in range(0, len(builtin_module_names)):
    sys.modules[i] = builtin_module_names[i]
print(sys.modules)
print()

for mod in sys.modules.keys():
    try:
        h = sys.modules[mod]
        m = str(h)
        exec(('import {}; print("[{}]\\n" + str(dir({})) + "\\n")').format(m, h, m))
    except Exception as error:
        print(error)