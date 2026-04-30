class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = 1
        prefix = 1
        output_array = []

        for idx, num in enumerate(nums):
            output_array.append(prefix)
            prefix *= num

        for idx in range(len(nums)-1, -1, -1):
            output_array[idx] = output_array[idx] * postfix
            postfix *= nums[idx]

        return output_array

        
        