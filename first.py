import inspect
import pyfirmata
import time
print('Starting...')
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
#variables
board = pyfirmata.Arduino('COM3')
led = board.get_pin('d:13:o')
#the loop
while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)
