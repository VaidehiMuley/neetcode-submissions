class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        res = []
        for l in range(len(nums)- k + 1):
            temp_res = float('-inf')
            for r in range(l, l+k):
                temp_res = max(temp_res,nums[r])
            res.append(temp_res)
        return res

