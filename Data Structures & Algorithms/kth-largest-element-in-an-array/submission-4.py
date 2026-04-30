class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        ## Quickselect
        def QuickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i] , nums[p]
                    p +=1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                # left
                return QuickSelect(l, p-1)
            elif k > p:
                # right
                return QuickSelect(p+1, r)
            else:
                return nums[p]
        return QuickSelect(0, len(nums)-1)
                 

        

        
