class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = len(nums)-1
        
        res = nums[0]
        while left_idx <= right_idx:
            
            ## check if array is already sorted, if so update res
            if nums[left_idx] < nums[right_idx]:
                res = min(res, nums[left_idx])
                break

            middle_idx = (left_idx + right_idx)//2
            res = min(res, nums[middle_idx])

            ## If middle is greater than left 
            if nums[left_idx] <= nums[middle_idx]:
                left_idx = middle_idx+1
                
                ## search in right portion
            else :
                # search in left portion
                right_idx = middle_idx-1
        return res
        


        