class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        ## recursive function
        def backtrack(i, subset): 
            ## Base case
            ## i = index
            if i == len(nums):
                res.append(subset[:])
                return

            ## Add the element
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            ## Skip the element
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            backtrack(i+1, subset)
        backtrack(0, [])
        return res
        

        