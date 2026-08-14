from deque import Deque

d = Deque()

assert d.is_empty()

d.add_rear(20)
d.add_front(10)
d.add_rear(30)

assert d.front() == 10
assert d.rear() == 30
assert d.size() == 3

assert d.remove_front() == 10
assert d.remove_rear() == 30
assert d.front() == 20
assert d.rear() == 20

d.clear()

assert d.is_empty()
assert d.remove_front() is None
assert d.remove_rear() is None

print("[OK] Deque")
print("ALL DEQUE TESTS PASSED")
