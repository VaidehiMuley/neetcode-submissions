class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = [-1,-1] 
        res_len = float("infinity")
        count,new_count = {},{}
        have = 0 
        for char in t:
            count[char] = 1 + count.get(char,0)

        need = len(count)
        for r in range(l,len(s)):
            new_count[s[r]] = 1+ new_count.get(s[r],0)
            if s[r] in count and new_count[s[r]] == count[s[r]]:
                have +=1
            while need == have: # basically means that count for each char has matched, we still want to move window to right to check if this can be minimised
                if (r - l + 1) < res_len:
                    res = [l,r]
                    res_len = r-l+1

                new_count[s[l]] -=1
                if s[l] in count and new_count[s[l]] < count[s[l]]:
                    have -=1
                l +=1
        l,r = res
        return s[l:r+1] if res_len != float("infinity") else ""    


            
                


        