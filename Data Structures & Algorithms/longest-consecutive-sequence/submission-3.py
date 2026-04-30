class Solution:
    def longestConsecutive(self, nums) -> int:
        sorted_list = sorted(nums)
        print(sorted_list)
        final_len = 1
        length = 1
        if len(nums) == 0 :
            return 0
        for i in range(len(sorted_list)-1):
            if (sorted_list[i+1] - sorted_list[i]) == 1:
                length +=1
                final_len = max(length, final_len)
                print(sorted_list[i],sorted_list[i+1],length,final_len)
            elif sorted_list[i] == sorted_list[i+1]:
                continue
            else:
                length = 1
        return final_len