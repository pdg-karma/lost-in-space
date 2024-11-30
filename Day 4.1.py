print('Starting...')
import pyfirmataConfig as config
import time
import shipClasses

board = config.board
it = config.pyfirmata.util.Iterator(board)
it.start()
Light = shipClasses.Light

#variables
lights = [Light("cabin",10,2), Light("storage",11,3), Light("cockpit",12,4)]

#the loop
while True:
    for light in lights:
        light.switch()
    time.sleep(0.1)