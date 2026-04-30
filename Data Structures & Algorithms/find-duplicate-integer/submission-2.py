class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## mark the already transversed ones as negative
        
        # seen = [0]*len(nums)

        # for num in nums:
        #     if seen[num] == 1:
        #         return num
        #     seen[num] = 1

        # Instead of using a seperate array, flip the index sign in the given array

        for num in nums:
            idx = abs(num) -1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1

    



        