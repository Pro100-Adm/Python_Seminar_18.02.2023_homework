class Matrix:

    def __init__(self, data_in_list):
        self.width = len(data_in_list[0])
        self.height = len(data_in_list)
        self.contents = []
        for i in range(self.height):
            self.contents.append([])
            for j in range(self.width):
                self.contents[i].append(data_in_list[i][j])

    def __str__(self):
        result = []
        for i in range(self.height):
            for j in range(self.width):
                result.append(f"{self.contents[i][j]} ")
            result.append('\n')
        return "".join(result)

    def __add__(self, other):
        result = []
        for i in range(self.height):
            result.append([])
            for j in range(self.width):
                result[i].append(self.contents[i][j] + other.contents[i][j])
        result_matr = Matrix(result)
        return result_matr


matr_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matr_2 = Matrix([[1, 2], [3, 4], [5, 6]])

print(type(matr_1))
print(matr_1)
print(type(matr_1 + matr_2))
print(matr_1 + matr_2)
