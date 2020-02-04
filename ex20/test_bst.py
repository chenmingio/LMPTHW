from bst import *

cities = BST(None, None)
cities.set(86, "China")
cities.set(49, "Germany")
cities.set(3, "USA")
cities.set(100, "Mars Urus")

def test_get():
    assert cities.get(86).val == "China"
    assert cities.get(49).val == "Germany"
    assert cities.get(3).val == "USA"
    assert cities.get(100).val == "Mars Urus"

def test_get_parent():
    assert cities.get_parent(49)[0].val == "China"
    assert cities.get_parent(49)[1] == "left"
    assert cities.get_parent(3)[0].val == "Germany"
    assert cities.get_parent(3)[1] == "left"
    assert cities.get_parent(100)[0].val == "China"
    assert cities.get_parent(100)[1] == "right"

def test_list():
    cities.list()

def test_delete():
    print("\n >>> before delete: ")
    cities.list()
    cities.delete(49)
    print("<<< after delete: ")
    cities.list()
    