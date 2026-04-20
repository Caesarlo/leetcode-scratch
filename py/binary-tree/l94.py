from typing import Optional, List
# Definition for a binary tree node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        self.traversal(root, res)
        return res

    def traversal(self, cur: TreeNode, res: List[int]):
        if cur is None:
            return
        self.traversal(cur.left, res)
        res.append(cur.val)
        self.traversal(cur.right, res)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res
