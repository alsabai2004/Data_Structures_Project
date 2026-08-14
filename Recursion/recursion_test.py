from recursion import factorial, fibonacci, sum_numbers, binary_search

assert factorial(0) == 1
assert factorial(5) == 120

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(7) == 13

assert sum_numbers(0) == 0
assert sum_numbers(5) == 15

data = [10, 20, 30, 40, 50]
assert binary_search(data, 30) == 2
assert binary_search(data, 99) == -1

print("[OK] Recursion")
print("ALL RECURSION TESTS PASSED")
