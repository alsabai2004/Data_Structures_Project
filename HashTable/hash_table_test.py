from hash_table import HashTable

h = HashTable(5)

assert h.is_empty()

assert h.insert("name", "Mohammed")
assert h.insert("age", 22)

assert h.search("name") == "Mohammed"
assert h.search("age") == 22
assert h.contains("name")
assert h.size() == 2

assert h.insert("age", 23) is False
assert h.search("age") == 23
assert h.size() == 2

assert h.delete("name")
assert not h.contains("name")
assert h.search("name") is None
assert h.size() == 1

assert not h.delete("unknown")

h.clear()

assert h.is_empty()
assert h.size() == 0

print("[OK] Hash Table")
print("ALL HASH TABLE TESTS PASSED")
