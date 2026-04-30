class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_check = list(''.join(i for i in s if i.isalnum()))
        i = 0
        j = len(to_check) -1
        while i < j:
            if to_check[i].lower() == to_check[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True



        