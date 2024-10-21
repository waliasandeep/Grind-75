class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallestArray(self, root: TreeNode, k: int) -> int:
        sorted_arr = []
        def dfs(node : TreeNode) -> None:
            if not node:
                return
            dfs(node.left)
            sorted_arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return sorted_arr[k-1]
    
    def kthSmallest(self, root : TreeNode, k : int) -> int:
        self.count = 0
        self.result = 0
        
        self.inorderTraversal(root, k)
        
        return self.result
    
    def inorderTraversal(self, node : TreeNode, k : int) -> None:
        if not node:
            return
        self.inorderTraversal(node.left, k)
        #print(node.val)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.inorderTraversal(node.right, k)

if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode()
    tree.val = 5
    tree.left = TreeNode(3)
    tree.right = TreeNode(6)
    tree.left.right = TreeNode(4)
    tree.left.left = TreeNode(2)
    tree.left.left.left = TreeNode(1)

    print(sol.kthSmallest(tree, 3))
    print(sol.kthSmallestArray(tree, 3))