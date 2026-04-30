class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.dict_ = {}
        # Iterate over each element, check if target - element is present in the dict where key is element and value is the index
        for idx,i in enumerate(nums):
            to_check = target - i
            if to_check in self.dict_.keys():
                return [self.dict_[to_check],idx]
            # if not move to next element and add the earlier element to dict
            self.dict_[i] = idx

        