from pyfirmataConfig import board

#classes
class Light:
    def __init__(self, room, light_pin_number, switch_pin_number):
        """
        Initialize the Light object with room name, light, and switch pin numbers.
        """
        self.room = room
        self.light_pin_number = light_pin_number
        self.switch_pin_number = switch_pin_number
        self.light_pin = None  # To store the light pin object
        self.switch_pin = None   # To store the switch pin object
        self.light_state = "off"
        self.switch_state = "off"

        # Initialize the pins on the board
        self.light_pin = board.get_pin(f'd:{self.light_pin_number}:o')  # light pin
        self.switch_pin = board.get_pin(f'd:{self.switch_pin_number}:i')    # switch pin

    def write(self, value):
        """
        Write a value (e.g., HIGH or LOW) to the light pin.
        """
        if self.light_pin:
            self.light_pin.write(value)
        else:
            print("light pin not initialized.")

    def read(self):
        """
        Read the value from the switch pin.
        """
        if self.switch_pin:
            return self.switch_pin.read()
        else:
            print("switch pin not initialized.")
            return None
    
    def switch(self):
        '''
        switch the lights on command
        '''
        if self.read() and self.switch_state == "off":
            if self.light_state == "off":
                self.write(1)
                self.light_state = "on"
            else:
                self.write(0)
                self.light_state = "off"
            self.switch_state = "on"
        if self.switch_state == "on" and not self.read():
            self.switch_state = "off"
