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

        print("i equals ", i)
        return i

    def invariant(self):
        """check 4 principles"""
        n = self.count()
        if n == 0:
            assert(self.begin is None)
            assert(self.end is None)
        else:
            assert(self.begin.prev is None)
            assert(self.end.next is None)
            if n == 1:
                assert(self.begin is self.end)

    def push(self, obj):
        """Appends a new value on the end of the list."""
        self.invariant()
        if self.count() == 0:
            new_node = DoubleLinkedListNode(obj, None, None)
            self.begin = new_node
            self.end = new_node
        else:
            new_node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = new_node
            self.end = new_node






