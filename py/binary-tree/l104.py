from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)

    def depth(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        left_d = self.depth(node.left)
        right_d = self.depth(node.right)
        return 1+max(left_d, right_d)
