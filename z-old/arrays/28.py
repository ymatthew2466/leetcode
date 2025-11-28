# 28. Find the Index of the First Occurrence in a String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        right ptr = left + len(needle)
        haystack[left: right] == needle -> valid
        '''

        for left in range(len(haystack)-len(needle)+1):
            right = left + len(needle) - 1
            if haystack[left: right+1] == needle:
                return left
        return -1