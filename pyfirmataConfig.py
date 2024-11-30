import inspect
import pyfirmata
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM3')
print('Board Set...')