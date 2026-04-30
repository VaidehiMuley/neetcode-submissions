class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m

            ## Left portion is sorted
            if nums[l] <= nums[m] :
                if (target > nums[m]) or (target < nums[l]):
                    # check right portion
                    l = m + 1
                else:
                    r = m -1
                
            ## Left portion is not sorted, therefore right is sorted
            else:
                if (target < nums[m]) or (target > nums[r]):
                    # Search left
                    r = m-1
                else:
                    # Search right
                    l = m + 1
                
        return res
        