"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    """ 
    This here initiates the number to begin the count.
    The number is also stored in the 'original' variable 
    so that when the reset function is called the 
    start varaible can be reset to the original function. 
    """
    def __init__(self, start): 
        self.start = start
        self.original = start

    """
    generate() will take the starting number and 
    save it to a variable. It then increments the 
    self,start variable and then displays the original 
    number. 
    """
    def generate(self):
        current = self.start
        self.start = self.start + 1
        return current
    
    """
    reset() will set self.start back to the original 
    starting number that was saved in self.original. 
    This allows for the generate() function to start
    from the beggining again. 
    """
    def reset(self): 
        self.start = self.original

