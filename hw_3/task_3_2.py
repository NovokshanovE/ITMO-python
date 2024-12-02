import numpy as np

class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __truediv__(self, other):
        return self.__class__(self.data / other.data)

    def __matmul__(self, other):
        return self.__class__(self.data @ other.data)

class FileIOWriteMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.data))

class PrettyPrintMixin:
    def __str__(self):
        return str(self.data)

class PropertyMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

class Matrix(ArithmeticMixin, FileIOWriteMixin, PrettyPrintMixin, PropertyMixin):
    def __init__(self, data):
        self.data = np.array(data)

def main():
    np.random.seed(0)

    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    import os
    os.makedirs('artifacts/3.2', exist_ok=True)

    (matrix1 + matrix2).save_to_file('artifacts/3.2/matrix+.txt')
    (matrix1 * matrix2).save_to_file('artifacts/3.2/matrix*.txt')
    (matrix1 @ matrix2).save_to_file('artifacts/3.2/matrix@.txt')

if __name__ == "__main__":
    main()