class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev
    
    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def count(self):
        """count the non-empty/None element"""
        cur_node = self.begin

        if cur_node is None:
            return 0

        i = 1
        while cur_node.next is not None:
            cur_node = cur_node.next
            i += 1

        # print("i equals ", i)
        return i

    def _invariant(self):
        """check 4 principles"""
        if self.begin == None:
            assert(self.end is None)
        elif self.begin.next == None:
            # only one element
            assert(self.begin is self.end)
        else:
            # these are requirment for all nodes, so put at begin
            assert(self.begin.prev is None)
            assert(self.end.next is None)


    def push(self, obj):
        """Appends a new value on the end of the list."""
        # process may include...
        # change pointer "end"
        # change next-pointer of vor-last
        # build new node
        # build new node pre and next part

        if self.begin == None:
            node = DoubleLinkedListNode(obj, None, None)
            self.begin = node
            self.end = node
        else:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node

    def pop(self):
        """Appends a new value on the end of the list."""

        if self.begin:
            node = self.end
            if self.begin == self.end:
                self.end = None
                self.begin = None
            else:
                self.end = node.prev
                self.end.next = None 
            return node.value
        else:
            return None


    def shift(self, obj):
        """Actually just another name for push"""

        # build new node
     
        # point self.beg to new node
        # point self.end to new node
        # or point self.end.prev to new node
        # point new node.next to self.begin
        # point self.begin.prev to new_node 

        new_node = DoubleLinkedListNode(obj, self.begin, None)
        n = self.count()
        # print("n is", n)

        # case n=0
        if n == 0:
            self.begin = new_node
            self.end = new_node

        elif n == 1:
            self.begin = new_node
            self.end.prev = new_node

        elif n > 1:
            self.begin.next.prev = new_node
            self.begin = new_node
        else:
            print("You are not supposed to reach here.")
            return None


    def unshift(self):
        """Removes the first item and returns it."""

        n = self.count()
        if n == 0:
            return None
        elif n == 1:
            rc = self.begin.value
            self.begin = None
            self.end = None
            return rc
        elif n > 1:
            rc = self.begin.value
            self.begin = self.begin.next
            # new begin's prev now is None
            self.begin.prev = None
            return rc
        else:
            print("You are not supposed to reach here.")
            return None

    def detach_node(self, node):
        """You'll need to use this operation someimes, but mostly inside remove(). It should take a node and detach it from the list, whether the node is at the front, end, or in the middle"""
        if self.begin == node:
            self.unshift()
        elif self.end == node:
            self.pop()
        else:
            node.prev.next = node.next.prev


    def remove(self, obj):
        """Finds a matching item and removes it from the list"""

        # find the rank of the node
        node = self.begin
        print(">>> begin node is ", node)
        count = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                node = node.next
                count += 1
                print(">>> node is now ", node, "and count is ", count)
        return -1
    
    def first(self):
        """Returns a *reference* to the first item, does not remove"""
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a *reference* to the last item, does not remove"""
        return self.end and self.end.value or None

    def get(self, index):
        """Get the value at index"""
        n = self.count()

        if index >= n:
            print("out of bound!")
            return None
        else:
            current_node = self.begin
            i = 0
            while i < index:
                current_node = current_node.next
                i += 1 
        
        return current_node.value
    
    def dump(self):
        node = self.begin
        # print("\n")
        while node:
            # print(">>> current node is ", node)
            node = node.next