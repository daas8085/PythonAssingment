def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example: Find the factorial of 5
print(factorial(5))
