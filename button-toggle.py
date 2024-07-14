import machine
import utime

button = machine.Pin(13, machine.Pin.IN)
led_yellow = machine.Pin(11, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

lights_on = False
led_yellow.value(0)
led_red.value(0)
led_blue.value(0)
count = 0

while True:
    if button.value() == 0:
        lights_on = not lights_on
        utime.sleep_ms(150)
  
    if lights_on:
        if button.value() == 0:
            lights_on = not lights_on
        led_blue.toggle()
        utime.sleep_ms(500)
        led_yellow.toggle()
        utime.sleep_ms(500)
        led_red.toggle()
        utime.sleep_ms(500)
    

        



        