# 107. 二叉树的层次遍历 II
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        queue = [root]
        while queue:
            size = len(queue)
            cur = []
            for _ in range(size):
                top = queue.pop(0)
                cur.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.insert(0, cur)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(12)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(root))
