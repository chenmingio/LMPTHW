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
        n = self.count()
        if n == 0:
            assert(self.begin is None)
            assert(self.end is None)
        else:
            # these are requirment for all nodes, so put at begin
            assert(self.begin.prev is None)
            assert(self.end.next is None)

            # special check for n=1
            if n == 1:
                assert(self.begin is self.end)

    def push(self, obj):
        """Appends a new value on the end of the list."""
        # process may include...
        # change pointer "end"
        # change next-pointer of vor-last
        # build new node
        # build new node pre and next part

        self._invariant()
        if self.count() == 0:
            new_node = DoubleLinkedListNode(obj, None, None)
            self.begin = new_node
            self.end = new_node
        else:
            new_node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = new_node
            self.end = new_node

    def pop(self):
        """Appends a new value on the end of the list."""

        # always conside when n=1 and n=0 boundary cases

        # when n > 1
        # return self.end.value
        # point self.end to vor-last node (if n=1, just point beg/end to None and return)
        # set vor-last node's next to None

        n = self.count()

        # case n=0
        if n == 0:
            return None

        rc = self.end.value

        # case n=1
        if n == 1:            
            self.end = None
            self.begin = None
            return rc
        elif n > 1:       
            self.end = self.end.prev
            self.end.next = None 
            return rc
        else:
            print("You are not supposed to reach here.")
            return None
        self._invariant()

    def shift(self, obj):
        """Actually just another name for push"""

        # build new node
     
        # point self.beg to new node
        # point self.end to new node
        # or point self.end.prev to new node
        # point new node.next to self.begin
        # point self.begin.prev to new_node 
        self._invariant()

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
        if node.prev is None and node.next is not None: # first node and not unique node
            node.next.prev = None
        elif node.next is None and node.prev is not None: # last node and not unique node
            node.prev.next = None
        elif node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else: # unique node case
            pass


    def remove(self, obj):
        """Finds a matching item and removes it from the list"""

        # find the rank of the node
        n = 0
        current_node = self.begin
        
        while current_node is not None:
            if current_node.value == obj:
                if n == 0: # node is first one. Besides detach, also point list_begin to current_node's next
                    self.begin = current_node.next
                if current_node.next == None: # node is last one. Besides detach, also point list_end to current_node's prev
                    self.end = current_node.prev
                self.detach_node(current_node)
                return n
            elif current_node.next is not None:
                current_node = current_node.next
                n += 1
            elif current_node.next is None:
                print("No matching found")
                return None

        print("Nothing to find in empty list")

    
    def first(self):
        """Returns a *reference* to the first item, does not remove"""
        return self.begin.value

    def last(self):
        """Returns a *reference* to the last item, does not remove"""
        return self.end.value

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