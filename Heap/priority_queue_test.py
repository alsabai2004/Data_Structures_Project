from priority_queue import PriorityQueue

q = PriorityQueue()

q.enqueue("Low", 3)
q.enqueue("High", 1)
q.enqueue("Medium", 2)

assert q.peek() == "High"
assert q.dequeue() == "High"
assert q.dequeue() == "Medium"
assert q.dequeue() == "Low"
assert q.is_empty()

print("[OK] Priority Queue")
print("ALL PRIORITY QUEUE TESTS PASSED")
