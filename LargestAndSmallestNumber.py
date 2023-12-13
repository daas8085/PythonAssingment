def find_largest_smallest(arr):
    if not arr:
        return None, None
    largest = smallest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

# Example: Find the largest and smallest numbers in an array
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest, smallest = find_largest_smallest(array)
print(f"Largest: {largest}, Smallest: {smallest}")
