class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt 

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):
    
    def __init__(self):
        self.top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        node = StackNode(obj, self.top)
        # print(">>> self.top is ", self.top)
        self.top = node

    def count(self):
        """Counts the number of elements in the stack"""
        node = self.top
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
        
    def pop(self):
        """Pops the value that is currently on the top of the stack"""
        if self.top:
            rc = self.top.value
            self.top = self.top.next
            return rc
        else:
            return None

    def toppest(self):
        """Returns the value that is currently on the top of the stack"""
        if self.top:
            return self.top.value
        else:
            return None
    
    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""

        if mark == "----":
            node = self.top
            print("\n")
            while node:
                print(">>> current node is ", node)
                node = node.next
        elif mark.split(" ")[0] == 'below':
            target_node = mark.split(" ")[1]
            print(">>> target node is ", target_node)
            node = self.top
            # turn node to target node
            while node != None and node.value != target_node:
                node = node.next
            while node:
                print(">>> current node is ", node)
                node = node.next
            