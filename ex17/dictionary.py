from dllist import *

class Dictionary(object):
    def __init__(self):
        MAX_NUM = 256
        self.map = DoubleLinkedList()
        for i in range(0, MAX_NUM):
            self.map.push(DoubleLinkedList())

    def get_bucket(self, key):
        bucket_id = hash(key) % 256
        return self.map.get(bucket_id)

    def get_slot(self, key):
        bucket = self.get_bucket(key)
        
        # missing bucket empty check here. Missing Guard is always necessary

        node = bucket.begin
        while node:
            if node.value[0] == key:
                return node
            else:
                node = node.next

        return node

    def set(self, key, val):
        # this is simplied into get_slot returning a tuple (bucket, node)
        node = self.get_slot(key)
        bucket = self.get_bucket(key)

        if node:
            node.value = (key, val)
        else:
            bucket.push((key, val))
    
    def get(self, key, default=None):
        node = self.get_slot(key)
        return node.value[1] if node else default

    def list(self):
        # print(">>> map type", self.map)
        bucket = self.map.begin
        while bucket and bucket.value:
            node = bucket.value.begin
            while node and node.value:
                print(node.value)
                node = node.next
            bucket = bucket.next
                 