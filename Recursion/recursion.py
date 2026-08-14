def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_numbers(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


def binary_search(data, target, left=0, right=None):
    if right is None:
        right = len(data) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if data[middle] == target:
        return middle

    if target < data[middle]:
        return binary_search(data, target, left, middle - 1)

    return binary_search(data, target, middle + 1, right)
