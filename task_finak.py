class OperationTable:
    def __init__(self, operation, num_rows=6, num_columns=6):
        self.operation = operation
        self.num_rows = num_rows
        self.num_columns = num_columns

    def print_table(self):
        for row in range(1, self.num_rows + 1):
            for col in range(1, self.num_columns + 1):
                result = self.operation(row, col)
                print(result, end="\t")
            print()


# Пример использования класса с операцией умножения
def multiply(a, b):
    return a * b

table = OperationTable(multiply)
table.print_table()