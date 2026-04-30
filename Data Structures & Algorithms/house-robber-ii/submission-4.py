class Solution:
    def helper(self,nums):
            rob1, rob2 = 0,0
            for i in nums:
                temp = max(i+rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[:-1]
        nums2 = nums[1:]
        return max(nums[0],self.helper(nums1), self.helper(nums2))

        