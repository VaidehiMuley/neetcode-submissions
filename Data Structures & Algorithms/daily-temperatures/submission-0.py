class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stash = []
        res = [0] * len(temperatures)
        for idx,i in enumerate(temperatures):
            while stash and i > stash[-1][0]:
                stashT, stashInd = stash.pop()
                if res[stashInd] == 0:
                    res[stashInd] = idx - stashInd
            stash.append((i, idx))
        return res

            

            
            
            
            



        