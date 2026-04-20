from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False
        outside = self.compare(left.left, right.right)
        insider = self.compare(left.right, right.left)
        return outside and insider
