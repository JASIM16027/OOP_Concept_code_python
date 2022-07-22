class Vector:
    def __init__(self, d):
        self._coord = [0] * d

    def __getitem__(self, item):
        return self._coord[item]

    def __setitem__(self, key, value):
        self._coord[key] = value


v1 = Vector(5)
v1.__setitem__(1, 6)
v1.__setitem__(2, 7)
v1.__setitem__(3, 10)
print(v1.__getitem__(2))

