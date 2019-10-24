import sorting
from dllist import DoubleLinkedList
from random import randint

max_number = 30

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        # print(i)
        numbers.shift(randint(0, 10000))
    numbers.dump()
    return numbers

def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value <= node.next.value:
            node = node.next
        else:
            return False
    return True

def test_bubble_sort():
    out_list = sorting.bubble_sort(random_list(max_number))
    return is_sorted(out_list)


def test_merge_sort():
    out_list = sorting.merge_sort(random_list(max_number))
    return is_sorted(out_list)


def test_is_sorted():
    test_numbers = DoubleLinkedList()
    for i in range(0, 100):
        test_numbers.push(i)
    assert is_sorted(test_numbers) == True
    assert is_sorted(random_list(100)) == False