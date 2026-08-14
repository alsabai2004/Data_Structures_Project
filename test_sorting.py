from Sorting.sorting import Sorting

data = [64, 25, 12, 22, 11, 90, 11]

expected = sorted(data)

assert Sorting.bubble_sort(data) == expected
assert Sorting.selection_sort(data) == expected
assert Sorting.insertion_sort(data) == expected
assert Sorting.merge_sort(data) == expected
assert Sorting.quick_sort(data) == expected

assert data == [64, 25, 12, 22, 11, 90, 11]
assert Sorting.is_sorted(expected)
assert not Sorting.is_sorted(data)

print("[OK] Bubble Sort")
print("[OK] Selection Sort")
print("[OK] Insertion Sort")
print("[OK] Merge Sort")
print("[OK] Quick Sort")
print("ALL SORTING TESTS PASSED")
