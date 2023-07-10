def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(result, end="\t")
        print()

# Пример использования функции с операцией умножения
def multiply(a, b):
    return a * b

print_operation_table(multiply)