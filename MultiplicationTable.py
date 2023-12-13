def print_multiplication_table(number, times):
    for i in range(1, times + 1):
        print(f"{number} x {i} = {number * i}")

# Example: Print the multiplication table for 5 up to 10 times
print_multiplication_table(5, 10)
