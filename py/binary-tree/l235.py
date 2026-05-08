# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if p.val < root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            # if left:
            return left
        elif p.val > root.val and q.val > root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            # if right:
            return right
        else:
            return root
