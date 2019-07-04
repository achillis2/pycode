# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
# Note:
#
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.



# Definition for a Node.

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            import pdb; pdb.set_trace()
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res

if __name__ == "__main__":
    leaf1 = Node(5, None)
    leaf2 = Node(6, None)
    med1 = Node(3, leaf1)
    med1.children = leaf2
    med2 = Node(2, None)
    med3 = Node(4, None)
    root = Node(1, med1)
    root.children = med2
    root.children = med3
    print(Solution().levelOrder(root))
