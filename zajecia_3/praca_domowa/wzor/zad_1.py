class SizeError(ValueError):
    pass

class Vector():
    def __init__(self, *args):
        self.coords = [x for x in args]

    def __str__(self):
        # lepiej użyć repr zamisat str, ale nie było poruszane na wykładzie
        return '{}({})'.format(
            self.__class__.__name__, ', '.join((str(x) for x in self.coords))
        )

    def __eq__(self, other):
        if len(self.coords) != len(other.coords):
            raise SizeError('Cannot compare vectors with different sizes')
        return self.coords == other.coords

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise SizeError('Cannot add vectors with different sizes')
        new_coords = [
            self.coords[i] + other.coords[i] for i in range(len(self.coords))
        ]
        return Vector(*new_coords)

    def __mul__(self, other):
        new_coords = [x * other for x in self.coords]
        return Vector(*new_coords)

    def __rmul__(self, other):
        return self * other

