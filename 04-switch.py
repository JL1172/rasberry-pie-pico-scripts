# out = gp 13

import machine
import utime

pin_13 = machine.Pin(13, machine.Pin.IN)
red_led = machine.Pin(15, machine.Pin.OUT)
