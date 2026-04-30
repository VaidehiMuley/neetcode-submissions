class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        if sorted(list_s) == sorted(list_t):
            return True
        return False

        