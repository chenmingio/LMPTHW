from dllist import *

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    # print(colors.end)
    colors._invariant()

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
    colors._invariant()

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None
    colors._invariant()


def test_shift():
    colors = DoubleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1

    colors.shift("Carbazole Violet")
    # print(colors.begin)
    # print(colors.end)
    assert colors.count() == 2

    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 1
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 0
    colors._invariant()

def test_remove():
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinon")
    assert colors.remove("Perinone") == 2
    colors.dump("after perinon")
    assert colors.remove("Nickle Yellow") == 1
    assert colors.remove("Zinc White") == 0


def test_first():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pathalo Green")
    assert colors.first() == "Pathalo Green"

def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Hansa Yellow"


def test_get():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None



# test_push()
# test_pop()
# test_shift()
# test_get()
# test_unshift()
# test_remove()
# test_first()
# test_last()