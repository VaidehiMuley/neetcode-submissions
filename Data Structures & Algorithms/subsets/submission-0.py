class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            ## base case:
            if i >= len(nums):
                ## Leaf node
                res.append(subset.copy())
                return
            ## Choice 1 : Include the number
            subset.append(nums[i])
            dfs(i + 1)

            ## Choce 2 : Exclude the number
            # Remove the last added number
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res

    
            
        