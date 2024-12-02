import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same size for addition.")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same size for element-wise multiplication.")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second.")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)

def main():
    np.random.seed(0)

    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    try:
        matrix_add = matrix1 + matrix2
        with open('artifacts/3.1/matrix+.txt', 'w') as f:
            f.write(str(matrix_add))
    except ValueError as e:
        print(f"Addition Error: {e}")

    try:
        matrix_elementwise_mul = matrix1 * matrix2
        with open('artifacts/3.1/matrix*.txt', 'w') as f:
            f.write(str(matrix_elementwise_mul))
    except ValueError as e:
        print(f"Element-wise Multiplication Error: {e}")

    try:
        matrix_matmul = matrix1 @ matrix2
        with open('artifacts/3.1/matrix@.txt', 'w') as f:
            f.write(str(matrix_matmul))
    except ValueError as e:
        print(f"Matrix Multiplication Error: {e}")

if __name__ == "__main__":
    main()