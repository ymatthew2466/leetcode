# 2486. Append Characters to String to Make Subsequence


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        Add chars, such that, T becomes a subsequence of S

        1. figure out how many chars of T is s.s. of S
            - for each s.s. overlapping char, pop it from s
            - now, we only care abt 0-th index
            - e.g. s = "coaching", t = "coding"
                - t = "ding" after initial prune
                - append "ding" to s
        2. append the rest
            - 
        '''
        
        if len(s) == 0:
            if len(t) == 0:
                return True
            return False
        
        # shave down T to remove all leading overlapping s.s. chars
        for char in s:
            if t != "" and t[0] == char:
                t = t[1:]
                
        return len(t)
        
        
# =============================== #
# test cases copied from LeetCode #
# =============================== #

if __name__ == "__main__":
    sol = Solution()

    # test case 1
    s1 = "coaching"
    t1 = "coding"
    assert sol.appendCharacters(s1, t1) == 4

    # test case 2
    s2 = "abcde"
    t2 = "a"
    assert sol.appendCharacters(s2, t2) == 0

    # test case 3
    s3 = "z"
    t3 = "abcde"
    assert sol.appendCharacters(s3, t3) == 5

    # test case 4: t is already subsequence of s
    s4 = "abac"
    t4 = "ac"
    assert sol.appendCharacters(s4, t4) == 0

    # test case 5: s and t are the same
    s5 = "abc"
    t5 = "abc"
    assert sol.appendCharacters(s5, t5) == 0

    print("All test cases passed!")


