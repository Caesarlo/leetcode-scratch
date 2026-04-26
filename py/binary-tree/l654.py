from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root_val = max(nums)
        root = TreeNode(root_val)
        index = nums.index(root_val)

        nums_left = nums[:index]
        nums_right = nums[index+1:]

        root_left = self.constructMaximumBinaryTree(nums_left)
        root_right = self.constructMaximumBinaryTree(nums_right)

        root.left = root_left
        root.right = root_right

        return root
