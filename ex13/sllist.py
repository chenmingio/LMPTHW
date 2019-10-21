class SLLNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
    
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SLL(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        '''Appends a new value on the end of the list.'''
        old_begin = self.begin
        self.begin = SLLNode(obj, old_begin)

    def pop(self):
        '''Removes the last item and returns it.'''
        if self.begin:
            ex_begin = self.begin
            self.begin = ex_begin.next
            return ex_begin.value
        else: 
            return None

    def shift(self, obj):
        '''Another name for push.'''
        last_node = self.search_n(0)
        last_node.next = SLLNode(obj, None)


    def unshift(self):
        '''Removes the first item and returns it.'''
        n = self.count()
        if n == 0:
            return None
        elif n == 1:
            result = self.begin.value
            self.begin = None
            return result
        elif n > 1:
            result = self.search_n(0).value
            self.search_n(1).next = None
            return result
        else:
            return None



    def count(self):
        '''Counts the number of elements in the list.'''
        count = 0
        current_node = self.begin
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search_n(self, n):
        '''return the nth elements of the list. 0-based. Return None if exeed the total length'''
        current_node = self.begin
        total = self.count() 
        # i is step
        i = total - n - 1

        if i < 0:
            return None

        while i > 0 and current_node is not None:
            current_node = current_node.next
            i -= 1
        return current_node



    def print_all(self):
        '''print all'''
        current_node = self.begin
        while current_node:
            print(current_node)
            current_node = current_node.next


    def search_first_value(self, value):
        '''return the nth when node value hits'''
        for i in range(0, self.count()):
            if self.search_n(i).value == value:
                return i

    def remove(self, obj):
        '''Finds a matching item and removes it form the list.'''
        i = self.search_first_value(obj)
        # print(i)

        # if the node is last node, take (n -1)th node as begin node
        if i  + 1 == self.count():
            self.begin = self.search_n(i - 1)
        # otherwise link (n + 1)th node to (n -1 )th node
        else:    
            self.search_n(i + 1).next = self.search_n(i - 1)

        return i


    def dump(self, mark):
        '''Debugging function that dumps the contents of the list.'''
        pass


    def first(self):
        '''Returns value of the first item, does not remove.'''
        first_node = self.search_n(0)
        # if current_node is not None
        if first_node:
            return first_node.value
        # if current_node is None
        else:
            return None


    def last(self):
        '''Returns a refernce to the last item, does not remove.'''
        # if current_node is not None
        last_node = self.begin
        if last_node:
            return last_node.value
        # if current_node is None
        else:
            return None

    def get(self, index):
        '''get the value at index.'''
        result_node = self.search_n(index) 
        if result_node:
            return result_node.value
        else:
            return None

