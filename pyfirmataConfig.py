import inspect
import pyfirmata
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM5')
def startIterator ():
    it = pyfirmata.util.Iterator(board)
    it.start()
startIterator()
print('Board Set...')