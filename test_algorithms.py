from Algorithms.searching import Searching

data = [10, 20, 30, 40, 50, 60, 70]

assert Searching.binary_search(data, 10) == 0
assert Searching.binary_search(data, 40) == 3
assert Searching.binary_search(data, 70) == 6
assert Searching.binary_search(data, 100) == -1

print("[OK] Binary Search")
print("ALL ALGORITHM TESTS PASSED")
