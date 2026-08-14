from HashTable.hash_table import HashTable

h = HashTable(5)
assert h.is_empty()
assert h.insert("A", 10)
assert h.insert("B", 20)
assert h.search("A") == 10
assert h.search("B") == 20
assert h.contains("A")
assert h.get_size() == 2
assert h.insert("A", 100) is False
assert h.search("A") == 100
assert h.delete("A")
assert not h.contains("A")
assert h.get_size() == 1
h.clear()
assert h.is_empty()
print("[OK] Hash Table")
print("HASH TABLE TEST PASSED")
