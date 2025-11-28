class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for char in s:
            pos = ord(char) - ord('a')
            if (pos>=0 and pos<26) or (char.isnumeric()):
                res += char
        l,r = 0, len(res)-1
        while l<r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True