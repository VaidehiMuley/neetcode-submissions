# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         counter = k
#         res = root.val

#         def dfs(node):
#             nonlocal counter, res

#             ## Base condition
#             if not node:
#                 return 

#             ## Go to left, reduce counter by 1
#             dfs(node.left)
#             counter -=1
#             if counter == 0:
#                 res = node.val
#                 return 
#             dfs(node.right)

#         dfs(root)
#         return res

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = root.val

        def dfs(node):
            nonlocal counter, res
            if not root:
                return None
            
            ### Inorder traversal
            dfs(root.left) 
            counter -=1
            if counter == 0:
                res = root.val 
                return res
                
            dfs(root.right)
        dfs(root)
        return res

            
            
        
        
        
        