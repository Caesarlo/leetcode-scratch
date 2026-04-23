from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_d = self.minDepth(root.left)
        right_d = self.minDepth(root.right)
        if root.left == None and root.right != None:
            return 1+right_d
        elif root.left != None and root.right == None:
            return 1+left_d
        return 1+min(left_d, right_d)
