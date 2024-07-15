import machine
import utime

button = machine.Pin(14, machine.Pin.IN)
red_led = machine.Pin(15, machine.Pin.OUT)

def toggle_led():
    red_led.toggle()

while True:
    if button.value() == 0:
        toggle_led()
        utime.sleep_ms(250)
    
        

