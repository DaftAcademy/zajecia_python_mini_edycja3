class Vector():
    def __init__(self, *args):
        self.coords = [x for x in args]

    def __str__(self):
        # lepiej użyć repr zamisat str, ale nie było poruszane na wykładzie
        return '{}({})'.format(
            self.__class__.__name__, ', '.join((str(x) for x in self.coords))
        )

    def __eq__(self, other):
        return self.coords == other.coords

    def __add__(self, other):
        n = max(len(self.coords), len(other.coords))
        new_coords = [self.coords[i] + other.coords[i] for i in range(n)]
        return Vector(*new_coords)

    def __mul__(self, other):
        new_coords = [x * other for x in self.coords]
        return Vector(*new_coords)

    def __rmul__(self, other):
        return self * other

v = Vector(1, 2)
assert v.coords == [1, 2]
v1 = Vector(3, 4)
v2 = Vector(3, 4)
assert v1 == v2
assert v2 == v1
assert v1 != v
assert v != v2
v = Vector(1, 2)
assert v * 5 == Vector(5, 10)
assert str(v) == 'Vector(1, 2)'

v = Vector()
assert str(v) == 'Vector()'

v = Vector(3.4)
assert str(v) == 'Vector(3.4)'

v1 = Vector(3.4)
v2 = Vector(3.6)

assert v1 + v2 == Vector(7.0)

v1 = Vector(*range(10))
v2 = Vector(*range(9, -1, -1))
assert str(v1) == 'Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)'
assert str(v2) == 'Vector(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)'
assert Vector(*[9]*10) == v1 + v2

v = Vector(*range(4))
assert v * 5 == Vector(0, 5, 10, 15)
