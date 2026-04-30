class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, i in enumerate(nums):

            ## Break if first element is positive - since it's the smallest element and if it's
            ## positive, all elements must be positive, therefore no need to check

            if i >0:
                break

            ## continue if the element is same as the prev element
            if idx > 0 and i == nums[idx -1]:
                continue
                
            ## assign left and right pointer
            l,r = idx+1, len(nums)-1

            while l < r:
                threesum_val = i+nums[l]+nums[r]
                
                ## If sum < 0 , increase left pointer
                if threesum_val < 0:
                    l +=1

                ## If sum > 0 , increase right pointer
                elif threesum_val > 0:
                    r -=1

                ## If sum = 0, then append to result
                else:
                    res.append([i, nums[l], nums[r]])
                    ## update and if nums[l] == nums[l+1], skip
                    l +=1
                    r -= 1
                    while nums[l] == nums[l-1] and l< r:
                        l +=1
        return res

        