import machine
import utime

button = machine.Pin(14, machine.Pin.IN)
red_led = machine.Pin(15, machine.Pin.OUT)

def toggle_led():
    red_led.toggle()
    
counter = 0

while True:
    if button.value() == 1:
        print("You pressed the button!")
        print(button.value())
        print(counter)
        counter+=1
        toggle_led()
        utime.sleep_ms(250)