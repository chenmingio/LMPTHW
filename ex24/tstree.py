class TSTreeNode(object):

    def __init__(self, key, value, low, eq, high):
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value

    def __repr__(self):
        return f"[key:{self.key}, val:{self.value}]" #, \n<---low:{self.low},\n---eq:{self.eq},\n--->high:{self.high}]"

class TSTree(object):
    def __init__(self):
        self.root = None


    def set(self, key, value):
        # break key string into list of chars
        keys = [x for x in key]
        # set list of chars into root node
        self.root = self._set(self.root, keys, value)

    def _set(self, node, keys, value):
        # next key = first char
        next_key = keys[0]

        # if root is empty
        if not node:
            # put first char as root node's key
            node = TSTreeNode(next_key, None, None, None, None)
        
        if next_key < node.key:
            # if first char < node's key
            node.low = self._set(node.low, keys, value)
        # just set node key as next_key    
        elif next_key == node.key:
            # still char remains
            if len(keys) > 1:
                # set eq node with next char
                node.eq = self._set(node.eq, keys[1:], value)
            else:
                # this is the leaf. Put value into this node
                node.value = value
        else:
            node.high = self._set(node.high, keys, value)

        return node

    def get(self, key):
        keys = [x for x in key]
        node = self._get(self.root, keys)
        # print(f">>> node returned is {node}.")
        return node and node.value or None

    def _get(self, node, keys):
        # print(f">>> keys is {keys }.")
        key = keys[0]
        # print(f">>> key is {key}.")
        # print(f">>> node is {node}.")

        if not node:
            return None

        if key < node.key:
            return self._get(node.low, keys)
        elif key == node.key:
            if len(keys) > 1:
                return self._get(node.eq, keys[1:])
            else:
                return node
        else:
            return self._get(node.high, keys)
        
    def find_all(self, key):
        result = []
        keys = [x for x in key]
        start = self._get(self.root, keys)
        if start:
            self._find_all(start.eq, result)
        # for node in result:
        #     print(node)
        return result
    
    def _find_all(self, node, result):

        if not node:
            return None
        if node:
            print(f">>> node is appended: {node}.")
            result.append(node)
        
        if node.low:
            self._find_all(node.low, result)
        elif node.eq:
            self._find_all(node.eq, result)
        elif node.high:
            self._find_all(node.high, result)
