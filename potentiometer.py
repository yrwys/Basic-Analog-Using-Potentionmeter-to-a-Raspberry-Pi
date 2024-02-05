from gpiozero import PWMLED, MCP3008
from time import sleep

pot = MCP3008(0)
led = PWMLED(21)

while True:
    if pot.value < 0.002:
        led.value = 0
    else:
        led.value = pot.value

    voltage = pot.value * 3.3
    analog_value = pot.raw_value
    print(f"Voltage: {voltage:.2f} V")
    print(f"Analog value: {analog_value}")
    print(f"LED Brightness: {int(led.value * 100)}%")
    print("====================")
    sleep(0.1)