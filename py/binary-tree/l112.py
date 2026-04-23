from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.traversal(root, targetSum)

    def traversal(self, node: Optional[TreeNode], sum_: int) -> bool:
        sum_ -= node.val

        if node.left == None and node.right == None:
            return sum_ == 0

        if node.left:
            if self.traversal(node.left, sum_):
                return True
        if node.right:
            if self.traversal(node.right, sum_):
                return True

        return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.traversal(root, targetSum-root.val)

    def traversal(self, node: Optional[TreeNode], sum_: int) -> bool:
        if not node.left and not node.right and sum_ == 0:  # 遇到叶子节点，并且计数为0
            return True
        if not node.left and not node.right:  # 遇到叶子节点直接返回
            return False

        if node.left:
            sum_ -= node.left.val
            if self.traversal(node.left, sum_):
                return True
            sum_ += node.left.val

        if node.right:
            sum_ -= node.right.val
            if self.traversal(node.right, sum_):
                return True
            sum_ += node.right.val

        return False
