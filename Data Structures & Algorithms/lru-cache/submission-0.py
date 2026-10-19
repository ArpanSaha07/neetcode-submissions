
# Time complexity: O(1) average per operation.
# Space complexity: O(capacity).

'''
We use a hash map to find any node by its key in O(1) average time, avoiding the O(n) search required by a linked list alone. We use a doubly linked list to insert, remove, and move nodes in O(1) time using their prev and next pointers, avoiding the O(n) shifting required by arrays or Python lists. Together, they allow us to implement both get() and put() in O(1) average time, while maintaining the least and most recently used entries.
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.capacity = capacity

        self.head = Node(0, 0)    # LRU is the next element after head
        self.tail = Node(0, 0)    # MRU is the prev element before tail

        self.head.next = self.tail
        self.tail.prev = self.head



    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)  # puts before the tail
            return node.value

        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)

        else:
            newNode = Node(key, value)
            self.insert(newNode)

            self.cache[key] = newNode

            if len(self.cache) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]

            
    def remove(self, node):
        
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):

        lastNode = self.tail.prev

        self.tail.prev = node
        node.next = self.tail

        lastNode.next = node
        node.prev = lastNode

        



        
