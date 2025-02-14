# Time Complexity : O(1), search in HM - constant, ading to head of LL - O(1), removing from tail of LL - O(1)
# Space Complexity : O(capacity) - hashmap and LL
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using hashmap for lookup, and doubly linked list for sequencing
# using dummy nodes for tail and head
# if we only use hashmap, we will be able to do search for key and value to put and update in O(1) time
# but to remove a node, we will have to do linear search
# then if we use a queue alone, we will be able to remove a node from the head and add at the end of the queue
# but then we will have to traverse the queue every time to add an element at the end
# if we use a singly linked list, we will not be able to remove
# if size of the hashmap == capacity, then we have to find the LRU, remove it and then do the operation
# every node we touch does to the head, so we are dding to the head
# and the LRU is at the prev of tail
# if key already exists, we will find the address of the node from the hashmap, go to the node and update the value
# then remove this node, and add it at the head of the LL - because we just performed an operation on it




class LRUCache(object):

    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # adding towards the head
        self.head = self.Node(-1, -1)
        # removing from the tail
        self.tail = self.Node(-1, -1)
        # hashmap to store key and the address of the node
        self.hashmap = {}
        # capacity
        self.capacity = capacity

        # empty Doubly LL
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # adding to the head operation
    def addToHead(self,node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    # remove the node operation
    def removeTheNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # key not present in the map
        if key not in self.hashmap:
            return -1
        
        # now it means the key exists in the map
        node = self.hashmap[key]

        # remove the node
        self.removeTheNode(node)
        # add to head        
        self.addToHead(node)

        # return the value of this key
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # either add or update

        # if key exists in hashmap - update the value, and move the node to head
        if key in self.hashmap:
            # update the value
            node = self.hashmap[key]
            node.value = value
            # remove the node
            self.removeTheNode(node)
            # and add to the head
            self.addToHead(node)
            return
        
        # adding a new node - we have to check capacity now

        # if capacity == size(hashmap)
        if len(self.hashmap) == self.capacity:
            # remove the LRU node, which is at the prev of tail
            tailprev = self.tail.prev
            self.removeTheNode(self.tail.prev)
            # imp to store the reference of tail.prev, because after we remove it, 
            # we wont be able to reference it to delete it's key from the hashmap
            self.hashmap.pop(tailprev.key)

        # if size of hashmap < capacity, create a node, add to head, add entry in hashmap
        # create new node
        node = self.Node(key, value)
        self.addToHead(node)
        self.hashmap[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)