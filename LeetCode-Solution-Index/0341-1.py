# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
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
        self.stack = nestedList[::-1]
        # 临时存放值的地方
        self.value = None

    def next(self):
        """
        :rtype: int
        """

        result = self.hasNext()

        if result:
            ret = self.value
            self.value = None
            return ret

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.value is not None:
            # 就不执行了，因为没有被取出来
            return True

        # 如果 self.value 为 None 的话
        # 就要从 stack 中弹出元素了

        while self.stack:
            top = self.stack.pop()
            # 如果栈中有元素，看看这个元素是什么
            if top.isInteger():
                # 是数字，就放在临时变量上
                self.value = top.getInteger()
                return True
            else:
                self.stack.extend(top.getList()[::-1])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
