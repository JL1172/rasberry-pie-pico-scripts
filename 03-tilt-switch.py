import utime
import machine

pin_nine = machine.Pin(9, machine.Pin.IN)

while True:
    if pin.nine.value() == 1:
        print("you tilted the bread board")
        