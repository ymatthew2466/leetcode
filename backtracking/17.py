# 17. Letter Combinations of a Phone Number

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dig = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
            
        res = []

        def bt(s: str):
            # base
            if (len(s) == len(digits)):
                res.append(s)
                return
            # recursive
            for char in dig[digits[len(s)]]:  # this is next char
                bt(s+char)
        
        for char in dig[digits[0]]:
            # string starter is letter of first digit
            bt(char)
        
        print(res)
        return res