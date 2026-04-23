from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root) == -1:
            return False
        else:
            return True

    def get_height(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        left_height = self.get_height(node.left)
        if left_height == -1:
            return -1

        right_height = self.get_height(node.right)
        if right_height == -1:
            return -1
        res = abs(right_height-left_height)
        if res > 1:
            return -1
        else:
            return max(left_height, right_height)+1
