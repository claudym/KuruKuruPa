from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # string representation of the object for inspection 
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)
    
    # arithmetic operator: add
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
