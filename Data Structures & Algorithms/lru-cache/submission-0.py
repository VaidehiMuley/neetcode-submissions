class Node:
    def __init__(self, key, val):
        self.key , self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        '''
        Steps:
            1. Get prev and next node
            2. Connect the prev node to next
            3. Connect next to prev
        '''
        nxt, prev = node.next, node.prev
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        '''
        Steps:
            1. Next = right, prev = right -1
            2. Connect prev to the new node 
            3. Connect next to new node 
        '''
        nxt, prev = self.right, self.right.prev
        node.next, node.prev = nxt, prev
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        '''
        Steps:
            1. Check if the key exists, if not return -1
            2. Given it exists, get the value of the required node
            3. Move the node to right by foll:
                a. Remove the node from current pos relative to left
                b. Insert it before right
        '''
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
          

    def put(self, key: int, value: int) -> None:
        '''
        Steps:
            1. Check if the key exists, if it does - remove it
            2. Add the key to cache
            3. Insert the node before right node
            4. Check if the len is exceeding capacity
            5. If yes - remove the LRU
        '''

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
