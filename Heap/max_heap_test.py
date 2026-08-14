from max_heap import MaxHeap

h = MaxHeap()

for value in [50, 20, 80, 10, 60, 90]:
    h.insert(value)

assert h.peek() == 90
assert h.extract_max() == 90
assert h.extract_max() == 80
assert h.extract_max() == 60
assert h.size() == 3

print("[OK] Max Heap")
print("ALL MAX HEAP TESTS PASSED")
