import numpy as np

class HashMixin:
    def hash(self):
        return int(self.data.sum() * self.data.size)

class Matrix(HashMixin):
    cache = {}

    def __init__(self, data):
        self.data = np.array(data)

    def __matmul__(self, other):
        h = (self.hash(), other.hash())
        if h in self.cache:
            print(f"Извлечение результата из кэша для хэша {h}")
            return self.cache[h]

        result_data = self.data @ other.data
        result = Matrix(result_data)
        self.cache[h] = result
        print(f"Кэширую результат для хэша {h}")
        return result

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.data))
        print(f"Сохранено {filename}")

    def __str__(self):
        return str(self.data)

def find_collision():
    np.random.seed(1)
    
    max_attempts = 10000
    attempts = 0
    
    print("Поиск коллизии между матрицами...")
    while attempts < max_attempts:
        attempts += 1
        
        matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
        matrix_c = Matrix(np.random.randint(0, 10, (10, 10)))
        
        if matrix_a.hash() == matrix_c.hash() and not np.array_equal(matrix_a.data, matrix_c.data):
            print(f"Коллизия найдена на попытке {attempts}. Хэш: {matrix_a.hash()}")
            
            while True:
                matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))
                matrix_d = Matrix(matrix_b.data.copy())
                
                if not np.array_equal((matrix_a @ matrix_b).data, (matrix_c @ matrix_d).data):
                    print(f"Произведения матриц различны для A @ B и C @ D на итерации проверки: {attempts}")
                    return matrix_a, matrix_b, matrix_c, matrix_d
    
    raise RuntimeError("Не удалось найти коллизию за разумное количество попыток")

def main():
    import os
    os.makedirs('artifacts/3.3', exist_ok=True)
    print("Директория artifacts/3.3 успешно создана.")

    try:
        A, B, C, D = find_collision()

        A.save_to_file('artifacts/3.3/A.txt')
        B.save_to_file('artifacts/3.3/B.txt')
        C.save_to_file('artifacts/3.3/C.txt')
        D.save_to_file('artifacts/3.3/D.txt')

        AB = A @ B
        CD = C @ D

        AB.save_to_file('artifacts/3.3/AB.txt')
        CD.save_to_file('artifacts/3.3/CD.txt')

        with open('artifacts/3.3/hash.txt', 'w') as f:
            f.write(f"Hash of AB: {AB.hash()}\n")
            f.write(f"Hash of CD: {CD.hash()}\n")
        print("Хэши произведений сохранены в artifacts/3.3/hash.txt")
    
    except RuntimeError as e:
        print(str(e))

if __name__ == "__main__":
    main()