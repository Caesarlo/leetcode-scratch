from typing import Optional, List
# Definition for a binary tree node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, cur: TreeNode, res: List[int]):
        if cur is None:
            return
        self.traversal(cur.left, res)
        self.traversal(cur.right, res)
        res.append(cur.val)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack[-1]
            stack.pop()
            if node is not None:
                res.append(node.val)
            else:
                continue
            stack.append(node.left)
            stack.append(node.right)
        res.reverse()
        return res
