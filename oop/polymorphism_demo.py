import math

class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius