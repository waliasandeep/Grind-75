class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, left_range, right_range):
            if not node:
                return True
            if not (left_range < node.val and node.val < right_range):
                return False
            return (helper(node.left, left_range, node.val) and helper(node.right, node.val, right_range))
        
        
        return helper(root, float('-inf'), float('+inf'))