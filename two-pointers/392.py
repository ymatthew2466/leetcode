# 392. Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        check if all chars from S are in T, IN ORDER
        '''
        if len(t) == 0:
            if len(s) == 0:
                return True
            return False
        
        # pointer 1
        s_index = 0

        # pointer 2
        for char in t:
            if s_index<len(s) and s[s_index] == char:
                # bounds check && check char from S and T in order
                s_index += 1
        
        # assume if s_index gets to end, all chars accounted for
        return s_index == len(s) 


# =============================== #
# test cases copied from LeetCode #
# =============================== #

if __name__ == "__main__":
    sol = Solution()

    # test case 1
    s1 = "abc"
    t1 = "ahbgdc"
    assert sol.isSubsequence(s1, t1) is True

    # test case 2
    s2 = "axc"
    t2 = "ahbgdc"
    assert sol.isSubsequence(s2, t2) is False

    # test case 3: empty s
    s3 = ""
    t3 = "ahbgdc"
    assert sol.isSubsequence(s3, t3) is True

    # test case 4: empty t
    s4 = "abc"
    t4 = ""
    assert sol.isSubsequence(s4, t4) is False

    # test case 5: s and t are same
    s5 = "abc"
    t5 = "abc"
    assert sol.isSubsequence(s5, t5) is True

    print("All test cases passed")


