class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            ## if a triplet's value is greater than target then filter out
            if t[0] > target[0] or t[1]> target[1] or t[2] > target[2]:
                continue

            ## For triplets which are valid, check if we can get all the target values
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3