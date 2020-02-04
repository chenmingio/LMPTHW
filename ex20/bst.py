class BST(object):
    def __init__(self, key, val, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

    def get(self, key):
        """Recursive implementation: Given a key, walk the tree to find the node, or return None if you reach a dead end."""
        print(">>> target key is ", key)
        print(">>> current node key is ", self.key)
        print(">>> current node val is ", self.val)
        if self.key == key or self.key is None:
            # print(">>> self returned with val: ", self.val)
            return self
        elif self.key > key:
            if self.left:
                return self.left.get(key)
            else:
                return None
        else:
            if self.right:
                return self.right.get(key)
            else:
                return None

    def get_parent(self, key):
        """Non-recursive implementation"""
#         Given a key, walk the tree to find the node, 
        node = self
        last_node = None
        loc = "Neutral"
        while node:
            # You go left if the given key is less-than the node’s key. 
            if node.key > key:
                last_node = node
                loc = "left"
                node = node.left
            # You go right if the key is greater-than the node’s key. 
            elif node.key < key:
                last_node = node
                loc = "right"
                node = node.right
            # If you read a node with no left or right, then you’re done and the node does not exist.
            elif node.key == key:
                print(">>> parent node with localtion", last_node, " ", loc)
                return last_node, loc
#       return None if you reach a dead end. 
        return None, None

    def set(self, key, val):
        if self.key == key or self.key is None:
            self.key = key
            self.val = val
        elif self.key > key:
            if self.left is None:
                self.left = BST(key, val)
            else:
                self.left.set(key, val)
        else:
            if self.right is None:
                self.right = BST(key, val)
            else:
                self.right.set(key, val)

    def delete(self, key):
        node = self.get(key)
        # 1. The D node is a “leaf” node because it has no children (not left or right). Just remove it from the parent.
        if node.left is None and node.right is None:
            parent_node, parent_loc = self.get_parent(key)
            if parent_node:
                print("-- parent key is ", parent_node.key)
                print("-- parent loc is ", parent_loc)
                if parent_loc == "left":
                    parent_node.left = None
                elif parent_loc == "right":
                    parent_node.right = None
        # 2. The D node has only one child (either left or right but not both). 
        # In that case you can simply move the value of this child to the D node, then delete the child. 
        # That effectively replaces the D node with the child (or, “moves the child up”).
        elif node.left is not None and node.right is None:
            parent_node, parent_loc = self.get_parent(key)
            if parent_node:
                target = getattr(parent_node, parent_loc)
                target = node.left        
        elif node.left is None and node.right is not None:
            parent_node, parent_loc = self.get_parent(key)
            if parent_node:
                target = getattr(parent_node, parent_loc)
                target = node.right
        else:
            minimum_node = self.find_minimum()
            node.key = minimum_node.key
            node.val = minimum_node.val
            self.delete(minimum_node.key)
    
    def list(self):
        """you have different way to wal through the tree."""
        if self == None:
            return self
        else:
            print("> key is ", self.key)
            print("> val is ",self.val)
        if self.left:
            print("> going left")
            self.left.list()
        if self.right:
            print("> going right")
            self.right.list()


    def find_minimum(self):
        if self.left is None:
            return self
        else:
            self.find_minimum()

    def replace_node_in_parent(self):
        pass

# 3. The D node has both a left and a right child, which means it’s time to do some major surgery. 
# First, find the minimum child of the D.right node called the successor. 
# Set the D.key to the successor.key
# do the same delete on this successor’s children using its key.