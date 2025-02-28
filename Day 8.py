print('Starting...')
from pyfirmataConfig import *
import time
from shipClasses import *

#variables
lights = [Light("red",11,2), Light("green",10,3), Light("blue",9,4)]

#the loop
while True:
    for light in lights:
        light.switch()
    time.sleep(0.1)