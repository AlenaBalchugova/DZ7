class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return self.quantity - other.quantity
        else:
            return "Вычитаемых ячеек больше чем имеющихся"

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        if self.quantity < other.quantity:
            return "В первой клетке ячеек > чем во второй"
        else:
            return round(self.quantity // other.quantity)

    def make_order(self, number_cell):
        self.number_cell = int(number_cell)
        if self.quantity > number_cell:
            rezult = "*" * self.number_cell
            whole = self.quantity // self.number_cell
            remains = self.quantity % self.number_cell
            rezult = rezult + "\n"
            rezult = rezult * whole
            if remains > 0:
                rezult += "*" * remains + "\n"
            return rezult + "\n"
        elif self.quantity == None:
            print("Ячейки отсутствуют")
        else:
            return "*" * self.quantity + "\n"

cell_1 = Cell(5)
cell_2 = Cell(3)
cell_3 = Cell(6)
cell_4 = Cell(4)
cell_5 = Cell(2)
cell_6 = Cell(12)
cell_7 = Cell(15)
cell_8 = Cell(36)

print(f"{cell_1} + {cell_2} = {cell_1 + cell_2}")
print(f"{cell_2} - {cell_5} = {cell_2 - cell_5}")
print(f"{cell_5} - {cell_1} = {cell_5 - cell_1}")
print(f"{cell_5} * {cell_2} = {cell_5 * cell_2}")
print(f"{cell_4} / {cell_3} = {cell_4 / cell_3}")
print(f"{cell_4} / {cell_5} = {cell_4 / cell_5}")
print(f"{cell_3} / {cell_4} = {cell_3 / cell_4}")

print(cell_1.make_order(6))
print(cell_6.make_order(5))
print(cell_7.make_order(5))
print(cell_8.make_order(10))

