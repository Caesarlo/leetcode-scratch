from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, cur: TreeNode, res: List[int]):
        if cur is None:
            return
        res.append(cur.val)
        self.traversal(cur.left, res)
        self.traversal(cur.right, res)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: List[TreeNode] = []
        res: List[int] = []
        stack.append(root)
        while stack:
            node = stack[-1]
            stack.pop()
            if node is not None:
                res.append(node.val)
            else:
                continue
            stack.append(node.right)
            stack.append(node.left)
        return res
