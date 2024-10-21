class TreeNode(object):
    def __init__(self, val =0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxDepth(tree))