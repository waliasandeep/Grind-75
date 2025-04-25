# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    
    tree.right= TreeNode(8)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)
    print(sol.lowestCommonAncestor(tree, tree.left, tree.right).val)
    print(sol.lowestCommonAncestor(tree, tree.left.right.left, tree.left.right.right).val)