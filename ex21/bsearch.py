def search_list(data, target):
    print(">>> data is ", data)
    print(">>> target is ", target)
    rc = search_recursive(data, target, 0, len(data) -1)
    if rc is not None:
        return target, rc
    else:
        return None, -1
    
    
def search_recursive(data, target, low, high):
    """the core recursive function for search_list"""
    # 5. Repeat, until either you find X or you have only 1 element left.
    if low >= high :
        # 2. If X == M, you’re done.
        if data[high] == target:
            return high
        else:
            return None
    # 1. Get the number in the middle of the list (M) and compare it to X.
    mid = (high + low)//2
    print("> mid now: ", mid)
    if target == data[mid]:
        return mid
    # 3. If X > M, then find the middle of M+1 to the end of the list.
    elif target > data[mid]:
        print(">>> enter into ", mid + 1, " - ", high)
        return search_recursive(data, target, mid + 1, high)
    # 4. If X < M, then find the middle of M-1 to the beginning of the list.
    elif target < data[mid]:
        print(">>> enter into ", low, " - ", mid - 1)
        return search_recursive(data, target, low, mid - 1)
    else:
        print(">>> you are not supposed to get here")


def search_list_iter(data, target):
    pass



