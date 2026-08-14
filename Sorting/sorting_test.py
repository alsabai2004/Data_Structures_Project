from sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

data = [64, 25, 12, 22, 11, 90, 34]
expected = [11, 12, 22, 25, 34, 64, 90]

assert bubble_sort(data) == expected
assert selection_sort(data) == expected
assert insertion_sort(data) == expected
assert merge_sort(data) == expected
assert quick_sort(data) == expected

assert data == [64, 25, 12, 22, 11, 90, 34]

print("[OK] Bubble Sort")
print("[OK] Selection Sort")
print("[OK] Insertion Sort")
print("[OK] Merge Sort")
print("[OK] Quick Sort")
print("ALL SORTING TESTS PASSED")
