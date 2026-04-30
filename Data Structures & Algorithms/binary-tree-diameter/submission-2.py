# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(current_root):
            if not current_root:
                return 0
            
            left = dfs(current_root.left)
            right = dfs(current_root.right)

            self.res = max(self.res, left+right)
            return 1+max(left,right)

        dfs(root)
        return self.res

        

        