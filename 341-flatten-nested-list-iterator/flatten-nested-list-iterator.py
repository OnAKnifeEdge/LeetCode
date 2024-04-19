# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self._flatten(nestedList)
        self.next_element = None
        self.is_end = None


    def _flatten(self, nestedList: [NestedInteger]):
        for nested in nestedList:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self._flatten(nested.getList())

    
    def next(self) -> int:
        if self.next_element is None:
            self.hasNext()
        result, self.next_element = self.next_element, None
        return result
        
    
    def hasNext(self) -> bool:
        if self.next_element:
            return True
        try:
            self.next_element = next(self.generator)
            return True
        except StopIteration:
            self.is_end = True
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())