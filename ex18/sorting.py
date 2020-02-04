from dllist import DoubleLinkedList

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort"""
    while True:
        number = numbers.begin
        count = numbers.count()
        for i in range(0, count):
            if number.value > number.next.value:
                temp = number.value
                number.value = number.next.value
                number.next.value = temp
        return numbers


def count(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count

def merge_sort(numbers):
# function merge_sort(list m)
    count = numbers.count()
    
    if count <= 1:
    # if length of m ≤ 1 then
        return numbers
    # return m
    # var left := empty list
    left_numbers = DoubleLinkedList()
    # var right := empty list
    right_numbers = DoubleLinkedList()
    # for each x with index i in m do
    i = 0
    node = numbers.begin
    # if i < (length of m)/2 then
    # add x to left
    for i in range(0, count):
        # print(">>> i=", i)
        rc = node.value
        if i < (count // 2):
            left_numbers.push(rc)
        # else
        # add x to right
        else:
            right_numbers.push(rc)
        node = node.next
    
    # left := merge_sort(left)
    left_numbers = merge_sort(left_numbers)
    # right := merge_sort(right)
    right_numbers = merge_sort(right_numbers)
    # return merge(left, right)
    return merge(left_numbers, right_numbers)


# function merge(left, right)
def merge(left, right):
    # var result := empty list
    rc = DoubleLinkedList()
    # while left is not empty and right is not empty do
    while left.begin and right.begin:
        # if first(left) ≤ first(right) then
        if left.begin.value <= right.begin.value:
            # append first(left) to result
            # left := rest(left)
            rc.push(left.unshift())
        # else
        else:
        # append first(right) to result
        # right := rest(right)
            rc.push(right.unshift())
    # while left is not empty do
    while left.begin:
        # append first(left) to result
        # left := rest(left)
        rc.push(left.unshift())
    # while right is not empty do
    while left.begin:
        # append first(right) to result
        #right := rest(right)
        rc.push(right.unshift())
    # return result
    return rc


# quickSort(array, leftmostIndex, rightmostIndex)
def quick_sort(array, lo, hi):
#   if (leftmostIndex < rightmostIndex)
    if (lo < hi):
        # pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
        p = partition(array, lo, hi)
        # quickSort(array, leftmostIndex, pivotIndex)
        quick_sort(array, lo, p-1)
        # quickSort(array, pivotIndex + 1, rightmostIndex)
        quick_sort(array, p + 1, hi)


# partition(array, leftmostIndex, rightmostIndex)
def partition(array, lo, hi):
    # print(">>>> Enter into partition")
    # print("> array section is ", array[lo:hi+1])
    # print("> low is ", lo)
    # print("> high is ", hi)
#   set rightmostIndex as pivotIndex
    pivot = array[hi]
    # print("> p value is ", pivot)
#   storeIndex <- leftmostIndex - 1
    i = lo -1
#   for i <- leftmostIndex + 1 to rightmostIndex
    for j in range (lo + 1, hi +1):
#     if element[i] < pivotElement
        if array[j] < pivot:
            i += 1
#           swap element[i] and element[storeIndex]
            array[j], array[i] = array[i], array[j]

#   swap pivotElement and element[storeIndex+1]
    array[i+1], array[hi] = array[hi], array[i+1]
    # print("<<<< Leave the partition.")
    # print("== array is now == ", array)
#   return storeIndex + 1
    return i + 1
