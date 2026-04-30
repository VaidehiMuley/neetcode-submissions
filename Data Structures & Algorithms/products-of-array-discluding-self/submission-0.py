class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_arr = []
        prefix = 1
        postfix = 1
        for idx,i in enumerate(nums):
            output_arr.append(prefix)
            prefix = prefix * i
        for i in range(len(nums)-1,-1,-1):
            output_arr[i] = output_arr[i]*postfix
            postfix = postfix*nums[i]
        return output_arr

        
        