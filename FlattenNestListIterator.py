# Time Complexity : O(1)
# Space Complexity : O(n), where n is the no of elements, and recursive stack space - O(l), where l is the no of nested lists => O(n + l)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using queue - not an optimal approach, we should take out ony the element that we absoultely need
# in this approach we we iterate over the nexted list, if he element is a list, we iterate over that until we get an integer, and then add that to the queue
# if element isint - we getint and put in queue
# for next we poll from the queue
# for has next - check if queue is empty 

from collections import deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = deque()
        self.flattenList(nestedList)

        

    def next(self):
        """
        :rtype: int
        """
        # the head of the queue, is the next element
        return self.q.popleft()


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.q) == 0:
            return False
        else:
            return True
        

    def flattenList(self, nestedList):
        # a list of nested integers
        # iterate over all elements in the nested list
        for el in nestedList:
            if el.isInteger():
                # the element if an integer
                self.q.append(el.getInteger())
            else:
                # element is a list
                # we get the list and then we recursively call this method
                # until we get a list just with integers, so that we can add them in queue
                self.flattenList(el.getList())



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())