
class Vector:

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('Invalid parameter type')

    def __len__(self):
        """Return the dimensions of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'
    
    @classmethod
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - self[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result


    def __rmul__(self, factor):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = factor*self[j]
        return result

    def __mul__(self, factor):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]*factor
        return result

    def __mul__(self, factor):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = factor*self[j]
        return result

    def __mul__(other1, other2):
        result = 0
        for j in range(len(self)):
            result[j] += other1[j] * other2[j]
        return result

