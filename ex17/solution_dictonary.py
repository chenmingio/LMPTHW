from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Initializeds a Map with the given numbers of buckets"""
        self.map = DoubleLinkedList()
        # use map as dictory container. It's actually a DLL
        for i in range(0, num_buckets):
            # this DLL has 256 slots/buckets
            self.map.push(DoubleLinkedList())
            # put 256 DLL inside this map DLL
    
    def hash_key(self, key):
        """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
        # transfer the "word key" to a "number key" using hash() function
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key)
        # return the number key
        return self.map.get(bucket_id) 
        # using the number key, search through the map DLL and get the DLL(bucket) we need

    def get_slot(self, key, default=None):
        # return value is the bucket and node(slot) to locate.
        """Returns either the bucket and node for a slot, or None, None""" 
        bucket = self.get_bucket(key)
        # using the key, through number key, get the reference to the DLL(bucket) we need

        if bucket:
            # make sure the bucket is not NULL? (Even it's a empty bucket DLL)
            node = bucket.begin
            # by default, will point to the first node
            i = 0

            # searching through this bucket DLL and find the node of same key. If
            while node:
                # as far as node is not empty, inside will be tuples... (key, value)
                if key == node.value[0]:
                    # if key is same as tuple's first key
                    return bucket, node
                    # this is the node(tuple) we need. return current DLL(bucket) and Node(tuple)
                else:
                    node = node.next
                    # else, search on the next node
                    i += 1

        # fall through for both if and while above
        return bucket, None
        # security. When it will happen?


    def get(self, key, default=None):
        """Gets the value in a bucket for a given key, or the default."""
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node
    
    def set(self, key, value):
        """Sets the key to the value, replacing and existing value."""
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))
    
    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next