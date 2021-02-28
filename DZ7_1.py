class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for el2 in range(len(other.my_list[el])):
                self.my_list[el][el2] = self.my_list[el][el2] + other.my_list[el][el2]
        return Matrix.__str__(self)


n = Matrix([[7, 12, 0],
            [4, -5, 7],
            [5, 7, 0],
            [0, 2, -1]])
new_n = Matrix([[1, 3, 1],
                [-0, 2, 7],
                [0, 9, 0],
                [3, -12, -1]])
print(n.__add__(new_n))