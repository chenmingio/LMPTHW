from stack import *

def test_push():
    books = Stack()
    assert books.count() == 0
    books.push("GEB")
    assert books.count() == 1
    books.push("SCIP")
    assert books.count() == 2
    books.push("Machine Learning")
    assert books.count() == 3
    
def test_pop():
    books = Stack()
    books.push("GEB")
    books.push("SCIP")
    books.push("Machine Learning")
    assert books.pop() == "Machine Learning"
    assert books.pop() == "SCIP"
    assert books.pop() == "GEB"
    assert books.pop() == None

def test_top():
    books = Stack()
    books.push("GEB")
    assert books.count() == 1
    assert books.toppest() == "GEB"
    books.push("SCIP")
    assert books.toppest() == "SCIP"
    books.push("Machine Learning")
    assert books.toppest() == "Machine Learning"

def test_dump():
    books = Stack()
    books.push("GEB")
    books.push("SCIP")
    books.push("Machine_Learning")
    books.dump("below Machine_Learning") # check the stdout
    books.dump("below SCIP") # check the stdout