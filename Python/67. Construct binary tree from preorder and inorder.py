# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        #if not preorder or not inorder:
        #    return None
        inorder_map = {}
        for index,val in enumerate(inorder):
            inorder_map[val] = index
        def buildTreeHelper(preorder_left : int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None
            root = TreeNode(val = preorder[preorder_left])
            index_root_inorder = inorder_map[root.val]
            length_left_subtree = index_root_inorder - inorder_left
            root.left = buildTreeHelper(preorder_left + 1, preorder_left + length_left_subtree, inorder_left, index_root_inorder - 1)
            root.right = buildTreeHelper(preorder_left + length_left_subtree +1, preorder_right, index_root_inorder + 1, inorder_right)
            
            return root
        
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
    
if __name__ == "__main__":
    sol = Solution()
    root = sol.buildTree([3,9,20,15,7],[9,3,15,20,7])
    print(root.val)
    